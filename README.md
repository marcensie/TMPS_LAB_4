# TMPS_LAB_4 - Task manager
## by Jardan Alexandru

## Objective :
Implement some behavioral design patterns in a project.

### Iterator: 
In the code, the Iterator class represents an iterator object. It maintains a reference to a collection of tasks (self.tasks) and keeps track of the current position within the collection using an index (self.index).
The next method returns the next element in the collection. It first checks if there is a next element by calling has_next(). If there is a next element, it retrieves the task at the current index, increments the index, and returns the task. If there are no more elements, it returns None.
This adheres to the Iterator pattern, which separates the logic of accessing and traversing a collection from the underlying implementation of the collection. It provides a way to iterate over elements in a collection without exposing its internal structure.
```
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
```

### Command: 
There are two command classes: AddTaskCommand and DeleteTaskCommand. Both of these classes encapsulate a specific action (add_task and delete_task, respectively) that can be executed on the task_collection object.
Each command class has an execute method that takes the task_collection object as an argument. When the execute method is called, it performs the corresponding action on the task_collection by calling the appropriate method (add_task or delete_task).
This structure adheres to the Command pattern, where actions are encapsulated as command objects, providing a way to decouple the invoker from the receiver and allowing for flexibility and extensibility in the system.
```
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

```

### Chain of Responsibility: 
There is a base Handler class that defines the common interface for all handlers in the chain. Each specific handler, such as DescHandler and StateHandler, inherits from the Handler class and overrides the search method to handle the search request based on its own criteria.
This structure adheres to the Chain of Responsibility pattern, where a series of handlers are chained together, and each handler has the option to handle the request or pass it along to the next handler in the chain.
```
class Handler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

    def search(self, tasks, query):
        if self.next_handler:
            return self.next_handler.search(tasks, query)
        return []

class DescHandler(Handler):
    def search(self, tasks, query):
        result = [task for task in tasks if task.desc.lower().find(query.lower()) != -1]
        if result:
            return result
        return super().search(tasks, query)

class StateHandler(Handler):
    def search(self, tasks, query):
        result = [task for task in tasks if task.state.lower().find(query.lower()) != -1]
        if result:
            return result
        return super().search(tasks, query)
```

### Memento: 
The Task class has two methods related to the Memento pattern: create_memento and restore_from_memento. The create_memento method returns a TaskMemento object that captures the current state of the task, including the description and state. The restore_from_memento method accepts a TaskMemento object and restores the task's state from the memento.

```
class Task:
...
    def create_memento(self):
        return TaskMemento(self.desc, self.state)

    def restore_from_memento(self, memento):
        self.desc = memento.desc
        self.state = memento.state

class TaskMemento:
    def __init__(self, desc, state):
        self.desc = desc
        self.state = state
...
def delete_task(self, index):
        if index < len(self.tasks):
            task = self.tasks.pop(index)
            memento = task.create_memento()
            self.undo_stack.append(memento)
            return task
        return None
    
    def undo_delete(self):
        if self.undo_stack:
            memento = self.undo_stack.pop()
            task = Task("", "")
            task.restore_from_memento(memento)
            self.tasks.append(task)
            return len(self.tasks) - 1, task
        return None, None

```




