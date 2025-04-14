# Beat Tag Builder

Beat Tag Builder is a Python-based GUI application designed to help Hip Hop Producers generate and manage tags for SoundCloud and YouTube. The application provides preset tag groups, tag processing, and cleaning functionalities to streamline the tagging process.

## Features

- **Preset Tag Groups**:
  - Mood & Instrumentation
  - Genre & Style Descriptors
  - Artist Type Beat Tags

- **Tag Processing**:
  - **SoundCloud**: Wraps tags in quotation marks and separates them with commas. Supports `#` and commas to trigger new tags.
  - **YouTube**: Removes `#` and quotation marks from tags and separates them with commas.

- **Tag Cleaning**:
  - Removes duplicate tags while preserving order.
  - Moves one-word tags to the end of the list.
  - Automatically processes tags as added.

- **Clipboard Support**:
  - Copy processed tags to the clipboard for ease of use.
  - Copy a customizable description from a text file (`description.txt`) to the clipboard.

- **Reset Functionality**:
  - Clears the result box and resets all button toggles.

- **Customizable Description**:
  - The application includes a `description.txt` file in the `src` folder. Users can edit this file to customize the description text that is copied to the clipboard when the "Copy Description" button is pressed.

- **Read-Only Result Box**:
  - The result box is read-only, allowing users to select and copy text but preventing typing or pasting.

## Installation

### This process will be streamlined with an installer shortly.

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/BeatTagBuilder.git
   cd BeatTagBuilder
   ```

2. Run the program:
   - Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

   - Run the following command to start the application:
     ```bash
     python src/BeatTagBuilder.py
     ```

## Customizing the Description Text

1. Open the `src/description.txt` file in a text editor.
2. Edit the content of the file to match your desired description.
3. Save the file. The updated content will be used when you press the "Copy Description" button.

## Usage

1. Select tags from the preset tag groups by clicking the buttons.
2. Tags will be added to the result box and automatically cleaned to remove duplicates as well as put one-word tags at the end of the tag body.
3. Use the "SoundCloud" or "YouTube" buttons to format tags for the respective platform.
4. Use the "Clean" button to manually clean tags if you see duplicates but this should happen automatically.
5. Use the "Copy" button to copy the processed tags to the clipboard.
6. Use the "Copy Description" button to copy the customizable description text to the clipboard.
7. Use the "Reset" button to clear the result box and reset all buttons.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue to suggest improvements or report bugs.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.