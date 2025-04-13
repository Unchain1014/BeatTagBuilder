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

- **Clipboard Support**:
  - Copy processed tags to the clipboard for ease of use.

- **Reset Functionality**:
  - Clears the result box and resets all button toggles.

## Installation
### This process will be streamlined with an installer shortly.

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/BeatTagBuilder.git
   cd BeatTagBuilder

2. Run the program:
   - Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

   - Run the following command to start the application:
     ```bash
     python src/main.py
     ```