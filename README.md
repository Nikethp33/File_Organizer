# 📂 File Organizer

A desktop application built with **Python and PySide6** that automatically organizes files into categories based on their file extensions.

The application allows users to preview planned file movements before execution, organize files safely, undo previous operations, and recover from failed undo operations.

---

## ✨ Features

- 📁 Select any folder to organize
- 🔍 Scan and preview files before making changes
- 🗂️ Automatically categorize files based on their extensions
- 🖼️ Organize Images
- 📄 Organize Documents
- 🎥 Organize Videos
- 🎵 Organize Audio files
- 📦 Organize Archives
- 🔢 Automatically handle duplicate filenames
- 👀 Preview all planned file movements
- ↩️ Undo the last organization operation
- 💾 Persistent operation history using JSON
- ⚠️ Error handling during file movement and undo operations
- 🗑️ Option to discard a remaining failed operation
- 🖥️ Expand the preview window for better visibility
- 🎨 Custom dark-themed PySide6 interface

---

## 🛠️ Technologies Used

- **Python**
- **PySide6**
- **pathlib**
- **shutil**
- **json**

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

The application follows a safe workflow to prevent accidental file movement.

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