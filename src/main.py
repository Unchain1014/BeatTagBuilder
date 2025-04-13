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

# Create the main application window
root = tk.Tk()
root.title("Beat Tag Builder")

# Prevent the user from resizing the window
root.resizable(False, False)

# Create a container frame with padding
container = tk.Frame(root, padx=25, pady=25)
container.pack(fill=tk.BOTH, expand=True)

# Define some preset tags for the FIRST row | Mood & Instrumentation
preset_tags_row1 = {
    "Lo-Fi": "#lofi #chillbeats #relaxingmusic #vibes",
    "Soulful": "#hiphop #beats #producer #rap #instrumentals",
    "Emotional": "#trap #beats #producer #808 #trapbeats",
    "Chill": "#boombap #oldschool #hiphop #producer",
    "Jazz": "#trap #beats #producer #808 #trapbeats",
    "Storytelling": "#boombap #oldschool #hiphop #producer",
    "Hard": "#lofi #chillbeats #relaxingmusic #vibes",
    "Gritty": "#lofi #chillbeats #relaxingmusic #vibes",
    "Guitar": "#boombap #oldschool #hiphop #producer",
    "Strings": "#lofi #chillbeats #relaxingmusic #vibes",
    "Brass": "#boombap #oldschool #hiphop #producer",
    "Piano": "#lofi #chillbeats #relaxingmusic #vibes"
}

# Define some preset tags for the SECOND row | Genre & Style Descriptors
preset_tags_row2 = {
    "Hip Hop": "#hiphop #beats #producer #rap #instrumentals",
    "Old School": "#trap #beats #producer #808 #trapbeats",
    "Boom Bap": "#boombap #oldschool #hiphop #producer",
    "Chill Hop": "#trap #beats #producer #808 #trapbeats",
    "Lo-Fi": "#boombap #oldschool #hiphop #producer"
}

# Define some preset tags for the THIRD row | Artist Type Beat Tags
preset_tags_row3 = {
    "Griselda": "#griselda type beat",
    "Nas": "#nas type beat",
    "MF DOOM": "#mfdoom type beat",
    "J Dilla": "#j dilla type beat",
    "Joey Bada$$": "#joey bada$$ type beat",
    "Freddie Gibbs": "#freddie gibbs type beat",
    "Isaiah Rashad": "#isaiah rashad type beat",
    "Aesop Rock": "#aesop rock type beat",
    "Mac Miller": "#mac miller type beat",
    "J Cole": "#j cole type beat",
    "Cypress Hill": "#cypress hill type beat",
}

def create_wrapping_buttons(frame, preset_tags, max_width=500):
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
row1_label = tk.Label(container, text="Mood & Instrumentation", font=("TkDefaultFont", 10, "bold"))
row1_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
button_frame_row1 = tk.Frame(container)
button_frame_row1.pack(pady=5)
buttons_row1 = create_wrapping_buttons(button_frame_row1, preset_tags_row1)

# Add a label and buttons for the SECOND row of presets | Genre & Style Descriptors
row2_label = tk.Label(container, text="Genre & Style Descriptors", font=("TkDefaultFont", 10, "bold"))
row2_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
button_frame_row2 = tk.Frame(container)
button_frame_row2.pack(pady=5)
buttons_row2 = create_wrapping_buttons(button_frame_row2, preset_tags_row2)

# Add a label and buttons for the THIRD row of presets | Artist Type Beat Tags
row3_label = tk.Label(container, text="Artist Type Beats", font=("TkDefaultFont", 10, "bold"))
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
    "Copy": copy_to_clipboard,
    "Reset": reset_tags
}
utility_buttons = create_single_row_buttons(container, utility_buttons_config)

# Start the GUI main loop
root.mainloop()