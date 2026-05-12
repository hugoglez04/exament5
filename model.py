class TaskModel:
    def __init__(self):
        # Lista que almacena las tareas [cite: 30]
        self.tasks = []

    def add_task(self, task):
        """Añade una tarea si no está vacía"""
        if task:
            self.tasks.append(task)
            return True
        return False

    def get_tasks(self):
        """Devuelve la lista actual de tareas"""
        return self.tasks