from PyQt6.QtWidgets import (
    QApplication,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QFileDialog,
)
import sys


class TextEditor(QWidget):
    def __init__(self):
        super(TextEditor, self).__init__()
        self.text = QTextEdit(self)
        self.clr_btn = QPushButton("Save")
        self.load_btn = QPushButton("Load")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.clr_btn)
        layout.addWidget(self.load_btn)

        self.clr_btn.clicked.connect(self.save_text)
        self.load_btn.clicked.connect(self.load_text)

        self.setLayout(layout)
        self.setWindowTitle("Text Editor")

    def save_text(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save File")
        if filename:
            with open(filename, "w") as f:
                f.write(self.text.toPlainText())

    def load_text(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Load File", "", "All Files (*);;Text Files (*.txt)"
        )
        if filename:
            with open(filename, "r") as f:
                file_text = f.read()
                self.text.setText(file_text)


app = QApplication(sys.argv)
writer = TextEditor()
writer.show()

sys.exit(app.exec())
