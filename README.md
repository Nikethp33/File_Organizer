# 📂 File Organizer

A desktop application built with **Python** and **PySide6** that automatically organizes files into categories based on their file extensions.

The application allows users to preview planned file movements before execution, organize files safely, undo previous operations, and recover from failed undo operations.

---

## ✨ Features

- 📁 Select any folder to organize
- 🔍 Scan and preview files before making changes
- 🗂️ Automatically categorize files based on their extensions
- 🖼️ Organize images
- 📄 Organize documents
- 🎥 Organize videos
- 🎵 Organize audio files
- 📦 Organize archives
- 🔢 Automatically handle duplicate filenames
- 👀 Preview planned file movements before confirmation
- ↩️ Undo the most recent organization operation
- 💾 Persistent operation history using JSON
- ⚠️ Error handling during file movement and undo operations
- 🗑️ Option to discard remaining failed operations from history
- 🖥️ Expandable preview window for better visibility
- 🎨 Custom dark-themed PySide6 interface

---

## 🛠️ Technologies Used

- Python
- PySide6
- `pathlib`
- `shutil`
- `json`

---

## 📁 Supported File Categories

| Category | Supported Extensions |
|---|---|
| 🖼️ Images | `.jpg`, `.jpeg`, `.png`, `.gif` |
| 📄 Documents | `.pdf`, `.docx`, `.txt` |
| 🎥 Videos | `.mp4`, `.mkv`, `.avi` |
| 🎵 Audio | `.mp3`, `.wav` |
| 📦 Archives | `.zip`, `.rar`, `.7z` |

---

# 🖥️ Application Workflow

The application follows a safe workflow to prevent accidental file movement:

```text
Select Folder
      ↓
Scan & Preview
      ↓
Review Planned Changes
      ↓
Confirm & Organise
      ↓
Files Are Moved
      ↓
Operation Saved to History
      ↓
Undo Available
```

## 🔍 Scan & Preview

Before organizing files, the application scans the selected folder and creates an organization plan.

The user can review every planned movement before confirming the operation.

Example:

```text
Files ready to organise: 5
Files skipped: 2

Planned moves:

photo.jpg  → Images/photo.jpg
report.pdf → Documents/report.pdf
song.mp3   → Audio/song.mp3
video.mp4  → Videos/video.mp4
archive.zip → Archives/archive.zip
```

This allows the user to verify changes before any files are moved.

---

## 🗂️ File Organization

Files are automatically moved into folders based on their extensions.

Example:

```text
Selected Folder
│
├── photo.jpg
├── report.pdf
├── song.mp3
├── movie.mp4
│
├── Images/
│   └── photo.jpg
│
├── Documents/
│   └── report.pdf
│
├── Audio/
│   └── song.mp3
│
└── Videos/
    └── movie.mp4
```

---

## 🔢 Duplicate Filename Handling

The application prevents files from being overwritten.

If a file with the same name already exists:

```text
photo.jpg
```

The application automatically generates a unique filename:

```text
photo (1).jpg
```

If necessary, it continues:

```text
photo (2).jpg
photo (3).jpg
```

This helps prevent accidental data loss.

---

## ↩️ Undo Functionality

Every successful organization operation is stored in a JSON history file.

Users can undo the most recent operation.

Example:

```text
Images/photo.jpg
        ↓
      Undo
        ↓
photo.jpg
```

The application processes file movements in reverse order to restore the previous state.

---

## ⚠️ Error Recovery

If an undo operation fails for one or more files, the application keeps track of the remaining failed operations.

The user can then:

- Resolve the issue manually and try the undo again
- Discard the remaining failed operation from history

This prevents a failed file from permanently blocking future undo operations.

---

## 💾 Persistent History

Operation history is stored using JSON.

This allows undo information to persist even after the application is closed.

Example structure:

```json
[
    [
        {
            "source": "example/photo.jpg",
            "destination": "example/Images/photo.jpg"
        }
    ]
]
```

---

## 🎨 User Interface

The application uses a custom dark-themed interface built with PySide6.

The interface includes:

- Folder selection
- Scan and preview functionality
- Activity and status display
- Confirmation before organizing
- Undo functionality
- Error recovery controls
- Expandable preview window

The interface also uses application state and button controls to guide the user through the workflow.

---

## 🖼️ Application Interface

![File Organizer Interface](app_interface.png)

---

## 📂 Project Structure

```text
File_Organizer/
│
├── main.py
├── file_organizer.py
├── app_interface.png
└── README.md
```

### `main.py`

Contains the PySide6 graphical user interface and application workflow.

### `file_organizer.py`

Contains the backend logic for:

- File scanning
- File categorization
- File movement
- Duplicate filename handling
- History management
- Undo operations
- Error handling

---

# ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Nikethp33/File_Organizer.git
```

### 2. Navigate to the project folder

```bash
cd File_Organizer
```

### 3. Install PySide6

```bash
pip install PySide6
```

---

# ▶️ Running the Application

Run:

```bash
python main.py
```

---

# 📦 Requirements

The project requires:

- Python
- PySide6

Install PySide6 using:

```bash
pip install PySide6
```

---

# 🧠 Concepts Practiced

This project was built as a practical exercise in several Python and GUI development concepts.

### Python

- Object-Oriented Programming
- Classes and methods
- File system operations
- `pathlib`
- `shutil`
- JSON data storage
- Exception handling
- Lists and dictionaries

### GUI Development

- PySide6
- Qt widgets
- Layout management
- Signals and slots
- Application state management
- Conditional button states
- GUI styling using Qt Style Sheets

---

# 🔮 Possible Future Improvements

Potential future additions could include:

- Support for custom file categories
- Settings page
- Drag-and-drop folder selection
- Progress indicators for large operations
- Multi-level undo/redo
- File search and filtering
- Light mode
- Custom themes
- Packaging the application as a standalone executable

---

# 👨‍💻 Author

**Niketh P**

Built as a Python project to practice:

- File handling
- Object-Oriented Programming
- Error handling
- Desktop GUI development using PySide6

---

⭐ If you found this project interesting, feel free to explore the code and suggest improvements!
