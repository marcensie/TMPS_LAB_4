class Iterator:
    def __init__(self, tasks):
        self.tasks = tasks
        self.index = 0

    def has_next(self):
        return self.index < len(self.tasks)

    def next(self):
        if self.has_next():
            task = self.tasks[self.index]
            self.index += 1
            return task
        return None
