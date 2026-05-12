from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QLabel

class TaskView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Tareas DESIN")
        self.resize(400, 400)

        self.layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.label = QLabel("Escribe una tarea y pulsa el botón:")
        self.task_input = QLineEdit()
        self.add_button = QPushButton("Añadir a la lista")
        self.task_list = QListWidget()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.task_input)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.task_list)