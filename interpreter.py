from chain import DescSearchHandler
from chain import StateSearchHandler

class QInterpreter:
    def __init__(self):
        self.handlers = {
            "desc": DescSearchHandler(),
            "state": StateSearchHandler(),
        }

    def interpret(self, query, task_collection):
        tokens = query.split(" ")
        field = tokens[0]
        search_term = " ".join(tokens[1:])

        if field in self.handlers:
            return self.handlers[field].search(task_collection.tasks, search_term)
        else:
            raise ValueError(f"Invalid query field: {field}")
