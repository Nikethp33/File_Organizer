# File Organizer

A desktop application built with **Python and PySide6** that automatically organizes files into categories based on their file extensions.

The application provides a graphical interface for selecting a folder, previewing planned file movements, organizing files, and undoing the most recent operation.

## Features

- Select any folder using a graphical folder picker
- Scan the selected folder and preview planned file movements
- Automatically organize supported files into categories
- Categorize files based on their extensions:
  - Images
  - Documents
  - Videos
  - Audio
  - Archives
- Prevent filename conflicts by generating unique filenames
- Confirm an operation before files are moved
- Display file activity and operation results in the GUI
- Undo the last recorded organization operation
- Store operation history using JSON
- Handle failed undo operations
- Discard a remaining failed operation when necessary
- Expand the Preview & Activity window for improved visibility

## Screenshots

Add screenshots of the application here if desired.

Example:

```text
screenshots/
├── main_window.png
└── expanded_preview.png
```

## Project Structure

```text
File_Organizer/
│
├── main.py
├── file_organizer.py
├── move_history.json
├── requirements.txt
└── README.md
```

> `move_history.json` is created and used to store file movement history for the undo feature.

## Technologies Used

- Python
- PySide6
- pathlib
- shutil
- json

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Nikethp33/File_Organizer.git
```

### 2. Navigate to the project folder

```bash
cd File_Organizer
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

If a `requirements.txt` file is not available, install PySide6 manually:

```bash
pip install PySide6
```

## Running the Application

Run the main application file:

```bash
python main.py
```

The File Organizer window should open.

## How to Use

### 1. Browse Folder

Click **Browse Folder** and select the folder you want to organize.

### 2. Scan & Preview

Click **Scan & Preview**.

The application will:

- Scan files in the selected folder
- Identify supported file extensions
- Create an organization plan
- Display the planned file movements
- Show the number of files ready to organize
- Show the number of skipped files

No files are moved during this stage.

### 3. Confirm & Organise

After reviewing the preview, click **Confirm & Organise**.

The application will move the supported files into their corresponding category folders.

### 4. Undo Last Operation

Click **Undo Last Operation** to reverse the most recently recorded organization operation.

The application uses the saved JSON history to determine where files should be moved back.

### 5. Discard Remaining Operation

If an undo operation encounters files that cannot be restored, the remaining operation can be discarded.

This allows the user to remove the problematic remaining history entry and continue using the application.

## File Categories

The organizer currently supports the following categories:

| Category | Supported Extensions |
|---|---|
| Images | `.jpg`, `.jpeg`, `.png`, `.gif` |
| Documents | `.pdf`, `.docx`, `.txt` |
| Videos | `.mp4`, `.mkv`, `.avi` |
| Audio | `.mp3`, `.wav` |
| Archives | `.zip`, `.rar`, `.7z` |

Files with unsupported extensions are skipped.

## How the Undo System Works

Each successful organization operation is stored in a JSON history file.

Conceptually, the history stores information like:

```json
[
    [
        {
            "source": "example/file.jpg",
            "destination": "example/Images/file.jpg"
        }
    ]
]
```

When **Undo Last Operation** is used, the application loads the most recent operation and attempts to move each file back to its original location.

If an undo operation fails for some files, the remaining failed movements can stay recorded so they can be handled appropriately. The user can also discard the remaining operation when manual intervention is required.

## Filename Conflict Handling

If a file with the same name already exists in the destination folder, the organizer generates a unique filename.

For example:

```text
photo.jpg
photo (1).jpg
photo (2).jpg
```

This helps prevent existing files from being overwritten.

## GUI Features

The application includes:

- Dark-themed interface
- Folder selection section
- Preview & Activity panel
- Scan & Preview button
- Confirm & Organise button
- Undo Last Operation button
- Discard Remaining Operation button
- Expand Preview option for improved readability

## Future Improvements

Possible future improvements include:

- Adding support for more file extensions
- Allowing users to create custom categories
- Adding drag-and-drop folder selection
- Adding a settings window
- Adding file icons to the preview
- Adding a progress bar for large operations
- Adding automated tests
- Adding logging
- Packaging the application as an executable

## What I Learned

This project helped me gain practical experience with:

- Object-oriented programming in Python
- File handling using `pathlib`
- Moving files using `shutil`
- JSON data storage
- Error handling with `try` and `except`
- Building desktop GUIs with PySide6
- Qt layouts and widgets
- Connecting buttons to Python functions using signals and slots
- Designing a multi-step user workflow
- Implementing persistent operation history
- Building an undo system for real file operations

## Author

**Niketh**

GitHub: https://github.com/Nikethp33

Project Repository: https://github.com/Nikethp33/File_Organizer

---

If you found this project useful, feel free to explore the repository and provide feedback.
