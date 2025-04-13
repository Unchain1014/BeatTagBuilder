import os
import tkinter as tk
from tkinter import messagebox

# Define a function to add a preset tag group to the message box
def add_tags(tags, button):
    current_text = result_box.get("1.0", tk.END).strip()  # Remove trailing newlines
    result_box.delete("1.0", tk.END)
    if current_text:  # Add a newline only if there's existing text
        current_text += "\n"
    result_box.insert(tk.END, current_text + tags)
    button.config(state=tk.DISABLED)  # Disable the button after it's pressed

# Add a reset function
def reset_tags():
    if messagebox.askyesno("Reset", "Are you sure you want to reset?"):
        # Clear the message window
        result_box.delete("1.0", tk.END)
        # Reset the state of all buttons
        for button in buttons_row1.values():
            button.config(state=tk.NORMAL)
        for button in buttons_row2.values():
            button.config(state=tk.NORMAL)
        for button in buttons_row3.values():
            button.config(state=tk.NORMAL)

# Global variable to track the last processing mode
last_processing_mode = "SoundCloud"  # Default to SoundCloud

# Function to process tags for SoundCloud
def process_soundcloud_tags():
    global last_processing_mode
    last_processing_mode = "SoundCloud"  # Update the last processing mode

    # Get the current content of the result box
    current_text = result_box.get("1.0", tk.END).strip()
    if not current_text:
        messagebox.showinfo("SoundCloud", "No tags to process!")
        return

    # Split the text into words and group them into tags
    words = current_text.replace(",", " ,").split()  # Treat commas as separate words
    tags = []
    current_tag = []

    for word in words:
        if word.startswith("#") or word == ",":  # Start a new tag on # or ,
            if current_tag:  # Save the previous tag
                tags.append(" ".join(current_tag))
            current_tag = [] if word == "," else [word]  # Start a new tag or reset for a comma
        else:
            current_tag.append(word)  # Add to the current tag

    if current_tag:  # Add the last tag
        tags.append(" ".join(current_tag))

    # Wrap each tag in quotes if not already quoted and join them with commas
    soundcloud_tags = ', '.join(
        tag if tag.startswith('"') and tag.endswith('"') else f'"{tag.strip("#")}"' for tag in tags
    )

    # Replace the content of the result box with the processed tags
    result_box.delete("1.0", tk.END)  # Clear the result box
    result_box.insert(tk.END, soundcloud_tags)  # Insert the processed tags

# Function to process tags for YouTube
def process_youtube_tags():
    global last_processing_mode
    last_processing_mode = "YouTube"  # Update the last processing mode

    # Get the current content of the result box
    current_text = result_box.get("1.0", tk.END).strip()
    if not current_text:
        messagebox.showinfo("YouTube", "No tags to process!")
        return

    # Split the text into words and group them into tags
    words = current_text.split()
    tags = []
    current_tag = []

    for word in words:
        if word.startswith("#"):  # Start a new tag
            if current_tag:  # Save the previous tag
                tags.append(" ".join(current_tag))
            current_tag = [word.lstrip("#").replace('"', '')]  # Start a new tag, remove # and all quotes
        else:
            current_tag.append(word.replace('"', ''))  # Add to the current tag, remove all quotes

    if current_tag:  # Add the last tag
        tags.append(" ".join(current_tag))

    # Join the tags with commas (no quotes added)
    youtube_tags = ', '.join(tags)

    # Replace the content of the result box with the processed tags
    result_box.delete("1.0", tk.END)  # Clear the result box
    result_box.insert(tk.END, youtube_tags)  # Insert the processed tags

# Function to clean duplicate tags and move one-word tags to the end
def clean_duplicates():
    global last_processing_mode

    # Force a pass of the last recorded processing mode
    if last_processing_mode == "SoundCloud":
        process_soundcloud_tags()
    elif last_processing_mode == "YouTube":
        process_youtube_tags()

    # Get the current content of the result box
    current_text = result_box.get("1.0", tk.END).strip()
    if not current_text:
        messagebox.showinfo("Clean Duplicates", "No tags to clean!")
        return

    # Split the tags by commas, strip whitespace, and remove duplicates
    tags = [tag.strip() for tag in current_text.split(",")]
    unique_tags = list(dict.fromkeys(tags))  # Preserve order while removing duplicates

    # Separate multi-word tags and one-word tags
    multi_word_tags = [tag for tag in unique_tags if " " in tag]
    one_word_tags = [tag for tag in unique_tags if " " not in tag]

    # Combine multi-word tags first, followed by one-word tags
    cleaned_tags = ", ".join(multi_word_tags + one_word_tags)

    # Replace the content of the result box with the cleaned tags
    result_box.delete("1.0", tk.END)  # Clear the result box
    result_box.insert(tk.END, cleaned_tags)  # Insert the cleaned tags

    messagebox.showinfo("Clean Duplicates", "Duplicates removed and one-word tags moved to the end!")

# Create the main application window
root = tk.Tk()
root.title("Beat Tag Builder")

# Set the application icon
icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
root.iconbitmap(icon_path)

# Prevent the user from resizing the window
root.resizable(False, False)

# Create a container frame with padding
container = tk.Frame(root, padx=25, pady=25)
container.pack(fill=tk.BOTH, expand=True)

# Define some preset tags for the FIRST row | Mood & Instrumentation
preset_tags_row1 = {
    "Piano": "#piano type beats #piano rap beats #free piano type beats",
    "Guitar": "#guitar type beats #guitar rap beats #free guitar type beats",
    "Chill": "#chill type beats #chill rap beats #free chill type beats",
    "Sad": "#sad type beats #sad rap beats #free sad type beats",
    "Happy": "#happy type beats #happy rap beats #free happy type beats",
    "Romantic": "#romantic type beats #romantic rap beats #free romantic type beats",
    "Angry": "#angry type beats #angry rap beats #free angry type beats"
}

# Define some preset tags for the SECOND row | Genre & Style Descriptors
preset_tags_row2 = {
    "Hard": "#hard type beats #hard instrumentals",
    "Aggressive": "#aggressive type beats #aggressive instrumentals",
    "Soulful": "#soulful type beats #soulful instrumentals",
    "Emotional": "#emotional type beats #emotional instrumentals",
    "West Coast": "#west coast type beats #west coast instrumentals",
    "Smooth": "#smooth type beats #smooth instrumentals",
    "Dark": "#dark type beats #dark instrumentals",
    "Freestyle": " #freestyle type beats #freestyle instrumentals",
    "Jazz": "#jazz type beats #jazz hip hop #jazz hop",
    "Latin": "#latin type beats #latin hip hop",
    "Old School": "#old school beats #old school type beats #old school hip hop",
    "Boom Bap": "#boom bap beats #boom bap instrumentals #boom bap",
    "Chill Hop": "#chill hop beats #chill hop instrumentals #chill hop",
    "Lofi": "#lofi hip hop #lofi beats #lofi instrumentals #lofi",
    "Hip Hop": "#hip hop beats #hip hop instrumentals #hip hop"
}

# Define some preset tags for the THIRD row | Artist Type Beat Tags
preset_tags_row3 = {
    "Eminem": "#eminem type beats #eminem instrumentals",
    "2Pac": "#2pac type beats #tupac type beats #2pac instrumentals #tupac instrumentals",
    "Notorious B.I.G.": "#notorious big type beats #notorious big instrumentals",
    "Kendrick Lamar": "#kendrick lamar type beats #kendrick lamar instrumentals",
    "Nas": "#nas type beats #nas instrumentals",
    "J Cole": "#j cole type beats #j cole instrumentals",
    "Griselda": "#griselda type beats #griselda instrumentals",
    "Kanye West": "#kanye west type beats #kanye west instrumentals",
    "MF DOOM": "#mfdoom type beats #mfdoom instrumentals",
    "J Dilla": "#j dilla type beats #j dilla instrumentals",
    "Joey Bada$$": "#joey bada$$ type beats #joey bada$$ instrumentals",
    "Freddie Gibbs": "#freddie gibbs type beats #freddie gibbs instrumentals",
    "Isaiah Rashad": "#isaiah rashad type beats #isaiah rashad instrumentals",
    "Aesop Rock": "#aesop rock type beats #aesop rock instrumentals",
    "Mac Miller": "#mac miller type beats #mac miller instrumentals",
    "Cypress Hill": "#cypress hill type beats #cypress hill instrumentals",
    "Common": "#common type beats #common instrumentals",
    "CaliberBeats": "#caliberbeats #caliber beats"
}

def create_wrapping_buttons(frame, preset_tags, max_width=750):
    buttons = {}
    current_width = 0
    row_frame = tk.Frame(frame)  # Create a new frame for the first row
    row_frame.pack(fill=tk.X, pady=5, expand=True)  # Pack the row frame with horizontal stretching

    for tag_name, tag_value in preset_tags.items():
        # Check if the current width exceeds the max width
        if current_width + 100 > max_width:  # Approximate button width + padding
            # Start a new row
            row_frame = tk.Frame(frame)
            row_frame.pack(fill=tk.X, pady=5, expand=True)
            current_width = 0  # Reset current width for the new row

        # Create a new button
        button = tk.Button(row_frame, text=tag_name)
        button.config(command=lambda tags=tag_value, btn=button: add_tags(tags, btn))  # Assign command after creation
        button.pack(side=tk.LEFT, padx=5, pady=5)
        buttons[tag_name] = button

        # Update the current width
        row_frame.update_idletasks()  # Ensure button dimensions are calculated
        current_width += button.winfo_reqwidth() + 10  # Approximate button width + padding

    return buttons

def create_single_row_buttons(frame, buttons_config):
    buttons = {}
    row_frame = tk.Frame(frame)  # Create a new frame for the row
    row_frame.pack(pady=5, anchor="center")  # Center the row frame without stretching it horizontally

    for button_text, button_command in buttons_config.items():
        # Create a button and pack it into the row frame
        button = tk.Button(row_frame, text=button_text, command=button_command)
        button.pack(side=tk.LEFT, padx=5, pady=5)  # Pack buttons side by side
        buttons[button_text] = button

    return buttons

# Add a label and buttons for the FIRST row of presets | Mood & Instrumentation
row1_label = tk.Label(container, text="1. Mood & Instrumentation", font=("TkDefaultFont", 10, "bold"))
row1_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
button_frame_row1 = tk.Frame(container)
button_frame_row1.pack(pady=5)
buttons_row1 = create_wrapping_buttons(button_frame_row1, preset_tags_row1)

# Add a label and buttons for the SECOND row of presets | Genre & Style Descriptors
row2_label = tk.Label(container, text="2. Genre & Style Descriptors", font=("TkDefaultFont", 10, "bold"))
row2_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
button_frame_row2 = tk.Frame(container)
button_frame_row2.pack(pady=5)
buttons_row2 = create_wrapping_buttons(button_frame_row2, preset_tags_row2)

# Add a label and buttons for the THIRD row of presets | Artist Type Beat Tags
row3_label = tk.Label(container, text="3. Artist Type Beats", font=("TkDefaultFont", 10, "bold"))
row3_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
button_frame_row3 = tk.Frame(container)
button_frame_row3.pack(pady=5)
buttons_row3 = create_wrapping_buttons(button_frame_row3, preset_tags_row3)

# Set up the result message box inside the container with a scrollbar
result_frame = tk.Frame(container)  # Create a frame to hold the Text widget and scrollbar
result_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(result_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

result_box = tk.Text(result_frame, height=10, width=50, wrap=tk.WORD, yscrollcommand=scrollbar.set)
result_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=result_box.yview)

# Add a copy button to copy the content of the message box
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_box.get("1.0", tk.END))
    messagebox.showinfo("Copied", "Tags copied to clipboard!")

# Add a row for Copy and Reset buttons
utility_buttons_config = {
    "SoundCloud": process_soundcloud_tags,
    "YouTube": process_youtube_tags,
    "Clean": clean_duplicates,
    "Reset": reset_tags,
    "Copy": copy_to_clipboard
}
utility_buttons = create_single_row_buttons(container, utility_buttons_config)

# Start the GUI main loop
root.mainloop()
