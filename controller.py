class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        # Conexión vital: al hacer clic, se ejecuta la lógica
        self.view.add_button.clicked.connect(self.handle_add_task)

    def handle_add_task(self):
        text = self.view.task_input.text()
        if self.model.add_task(text):
            self.view.task_list.addItem(text) # Actualiza la vista
            self.view.task_input.clear()      # Limpia el campo