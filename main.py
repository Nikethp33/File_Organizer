import sys
from file_organizer import FileOrganiser

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog,
    QTextEdit,
    QFrame,
    QDialog
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Organizer")
        self.resize(450, 650)

        self.selected_folder = None
        self.planned_moves = []

        #central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        main_layout.setContentsMargins(30, 25, 30, 25)
        main_layout.setSpacing(20)
        
        #Header
        title = QLabel("File Organizer")
        title.setObjectName("title")
        subtitle = QLabel("Automatically organize your files into categories")
        subtitle.setObjectName("subtitle")
        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        #Folder
        folder_frame = QFrame()
        folder_layout = QVBoxLayout()

        folder_frame.setLayout(folder_layout)

        folder_title = QLabel("Selected Folder")
        folder_title.setObjectName("section_title")

        self.folder_path_label = QLabel(
            "No folder selected"
        )
        self.folder_path_label.setObjectName("folder_path")
        

        browse_button = QPushButton("Browse Folder")
        browse_button.clicked.connect(self.browse_folder)

        folder_layout.addWidget(folder_title)
        folder_layout.addWidget(self.folder_path_label)
        folder_layout.addWidget(browse_button)

        main_layout.addWidget(folder_frame)


        # PREVIEW SECTION

        preview_title = QLabel("Preview & Activity")
        preview_title.setObjectName("section_title")

        self.preview_box = QTextEdit()
        self.preview_box.setReadOnly(True)

        main_layout.addWidget(preview_title)
        main_layout.addWidget(self.preview_box)
        self.expand_preview_button = QPushButton(
            "Expand Preview"
        )

        self.expand_preview_button.clicked.connect(
            self.expand_preview
        )

        main_layout.addWidget(
            self.expand_preview_button
        )

        # ACTION BUTTONS

        action_layout = QHBoxLayout()

        self.organise_button = QPushButton("Scan & Preview")
        self.organise_button.clicked.connect(self.organise_files)

        self.confirm_button = QPushButton(
            "Confirm & Organise"
        )
        self.confirm_button.setEnabled(False)
        self.confirm_button.clicked.connect(
            self.confirm_organise
        )

        self.undo_button = QPushButton(
            "Undo Last Operation"
        )
        self.undo_button.clicked.connect(
            self.undo_last_operation
        )

        self.organise_button.setObjectName("scan_button")
        self.confirm_button.setObjectName("confirm_button")
        self.undo_button.setObjectName("undo_button")

        action_layout.addWidget(self.organise_button)
        action_layout.addWidget(self.confirm_button)
        action_layout.addWidget(self.undo_button)

        main_layout.addLayout(action_layout)

        # DISCARD BUTTON

        self.ignore_undo = QPushButton(
            "Discard Remaining Operation"
        )
        self.ignore_undo.setObjectName("danger_button")

        self.ignore_undo.setEnabled(False)

        self.ignore_undo.clicked.connect(
            self.ignore_undo_operation
        )

        main_layout.addWidget(self.ignore_undo)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e1e;
            }

            QWidget {
                color: #e6e6e6;
                font-size: 14px;
            }

            QLabel#title {
                font-size: 30px;
                font-weight: bold;
                color: #ffffff;
            }

            QLabel#subtitle {
                font-size: 15px;
                color: #a0a0a0;
            }

            QLabel#section_title {
                font-size: 17px;
                font-weight: bold;
                color: #ffffff;
            }

            QFrame {
                background-color: #292929;
                border: 1px solid #3a3a3a;
                border-radius: 10px;
                padding: 10px;
            }

            QPushButton {
                background-color: #595959;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 16px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #4d4d4d;
            }

            QPushButton:pressed {
                background-color: #595959;
            }

            QPushButton:disabled {
                background-color: #444444;
                color: #888888;
            }

            QTextEdit {
                background-color: #252525;
                border: 1px solid #3a3a3a;
                border-radius: 8px;
                padding: 10px;
                color: #dddddd;
            }

            QLabel#folder_path {
                background-color: #202020;
                border-radius: 6px;
                padding: 10px;
                color: #bdbdbd;
            }
            QPushButton#danger_button {
                background-color: #595959;
            }

            QPushButton#danger_button:hover {
                background-color: #4d4d4d;
            }

            QPushButton#scan_button {
                background-color: #595959;
            }

            QPushButton#scan_button:hover {
                background-color: #4d4d4d;
            }

            QPushButton#confirm_button {
                background-color: #595959;
            }

            QPushButton#confirm_button:hover {
                background-color: #4d4d4d;
            }

            QPushButton#undo_button {
                background-color: #595959;
            }

            QPushButton#undo_button:hover {
                background-color: #4d4d4d;
            }
        """)

    def expand_preview(self):

        preview_window = QDialog(self)

        preview_window.setWindowTitle(
            "Preview & Activity"
        )

        preview_window.resize(900, 700)

        layout = QVBoxLayout()

        preview_window.setLayout(layout)

        expanded_preview = QTextEdit()

        expanded_preview.setReadOnly(True)

        expanded_preview.setText(
            self.preview_box.toPlainText()
        )

        layout.addWidget(expanded_preview)

        preview_window.exec()



    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(
            self,
            "Select Folder"
        )

        if folder:

            self.selected_folder = folder

            self.folder_path_label.setText(folder)

            self.planned_moves = []

            self.confirm_button.setEnabled(False)

            self.preview_box.clear()

            self.preview_box.append(
                "Folder selected. Click 'Scan & Preview' to continue."
            )

    def organise_files(self):

        if not self.selected_folder:

            self.preview_box.clear()

            self.preview_box.append(
                "Please select a folder first"
            )

            return

        self.preview_box.clear()

        organizer = FileOrganiser(self.selected_folder)

        self.planned_moves, skipped_files = organizer.create_plan()

        if not self.planned_moves:

            self.preview_box.append(
                "No files found to organise"
            )

            self.confirm_button.setEnabled(False)

            return
        self.preview_box.append(
            f"Files ready to organise: {len(self.planned_moves)}"
        )

        self.preview_box.append(
            f"Files skipped: {len(skipped_files)}\n"
        )
        
        self.preview_box.append("Planned moves:\n")

        for source, destination in self.planned_moves:

            self.preview_box.append(
                f"{source.name} → {destination}"
            )

        self.confirm_button.setEnabled(True)
            



    def confirm_organise(self):

        if not self.planned_moves:
            print("No organisation plan available")
            self.preview_box.clear()
            self.preview_box.append("No organisation plan available")
            return

        organizer = FileOrganiser(self.selected_folder)

        move_history, errors = organizer.execute_plan(self.planned_moves)

        if move_history:
            organizer.save_history(move_history)

        print(f"Moved {len(move_history)} files")

        self.preview_box.clear()
        self.preview_box.append("Files organised")
        self.preview_box.append(f"Files moved: {len(move_history)}")


        if errors:

            self.preview_box.append(
                f"\nErrors: {len(errors)}"
            )

        else:

            self.preview_box.append(
                "\nNo errors occurred"
            )

        self.planned_moves = []

        self.confirm_button.setEnabled(False)


    def undo_last_operation(self):

        if not self.selected_folder:

            self.preview_box.clear()
            self.preview_box.append(
                "Please select a folder first."
            )
            return

        organizer = FileOrganiser(self.selected_folder)

        move_history = organizer.load_history()

        if not move_history:

            self.preview_box.clear()
            self.preview_box.append(
                "No recorded history found."
            )
            return

        failed_undos, errors = organizer.undo(move_history)

        organizer.update_last_operation(failed_undos)

        self.preview_box.clear()

        successful_undos = (
            len(move_history) - len(failed_undos)
        )

        self.preview_box.append("Undo Complete!")
        self.preview_box.append(
            f"Files undone: {successful_undos}"
        )

        if errors:

            self.preview_box.append(
                f"\nErrors: {len(errors)}"
            )

            self.ignore_undo.setEnabled(True)

        else:

            self.preview_box.append(
                "\nNo errors occurred!"
            )

            self.ignore_undo.setEnabled(False)

    
    def ignore_undo_operation(self):

        if not self.selected_folder:

            self.preview_box.clear()

            self.preview_box.append(
                "Please select a folder first."
            )

            return

        organizer = FileOrganiser(
            self.selected_folder
        )

        organizer.discard_last_operation()

        self.preview_box.clear()

        self.preview_box.append(
            "Remaining operation discarded."
        )

        self.preview_box.append(
            "You can continue using the organizer."
        )

        self.ignore_undo.setEnabled(False)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()