from iterator import Iterator
from task import Task

class TaskCollection:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, index):
        if index < len(self.tasks):
            task = self.tasks.pop(index)
            memento = task.create_memento()
            self.undo_stack.append(memento)
            return task
        return None

    def get_iterator(self):
        return Iterator(self.tasks)
    
    def undo_delete(self):
        if self.undo_stack:
            memento = self.undo_stack.pop()
            task = Task("", "")
            task.restore_from_memento(memento)
            self.tasks.append(task)
            return len(self.tasks) - 1, task
        return None, None
    
    def show_all_tasks(self):
        print("All Tasks:")
        for task in self.tasks:
            print(f"{task.desc} - {task.state}")
    
