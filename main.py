import sys
from PySide6.QtWidgets import QApplication
from model import TaskModel
from view import TaskView
from controller import TaskController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Instanciamos las tres capas del MVC
    model = TaskModel()
    view = TaskView()
    controller = TaskController(model, view)
    
    view.show()
    sys.exit(app.exec())