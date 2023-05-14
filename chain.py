class Handler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

    def search(self, tasks, query):
        if self.next_handler:
            return self.next_handler.search(tasks, query)
        return []

class DescSearchHandler(Handler):
    def search(self, tasks, query):
        result = [task for task in tasks if task.desc.lower().find(query.lower()) != -1]
        if result:
            return result
        return super().search(tasks, query)

class StateSearchHandler(Handler):
    def search(self, tasks, query):
        result = [task for task in tasks if task.state.lower().find(query.lower()) != -1]
        if result:
            return result
        return super().search(tasks, query)

