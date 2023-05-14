class AddTaskCommand:
    def __init__(self, task):
        self.task = task

    def execute(self, task_collection):
        task_collection.add_task(self.task)
        
class DeleteTaskCommand:
    def __init__(self, index):
        self.index = index

    def execute(self, task_collection):
        del task_collection.tasks[self.index]
