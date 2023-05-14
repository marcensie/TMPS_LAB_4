class Task:
    def __init__(self, desc, state):
        self.desc = desc
        self.state = state

    def create_memento(self):
        return TaskMemento(self.desc, self.state)

    def restore_from_memento(self, memento):
        self.desc = memento.desc
        self.state = memento.state

class TaskMemento:
    def __init__(self, desc, state):
        self.desc = desc
        self.state = state
