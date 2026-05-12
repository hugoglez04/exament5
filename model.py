class TaskModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task.strip(): # Evita añadir tareas vacías
            self.tasks.append(task)
            return True
        return False