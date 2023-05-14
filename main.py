from task import Task
from task_collection import TaskCollection
from interpreter import QInterpreter
from command import AddTaskCommand
from command import DeleteTaskCommand

def main():
    task_collection = TaskCollection()
    query_interpreter = QInterpreter()

    while True:
        command = input(": ")

        if command == "add":
            desc = input("task: ")
            state = input("state: ")
            add_task_command = AddTaskCommand(Task(desc, state))
            add_task_command.execute(task_collection)

        elif command == "del":
            id = int(input("id: "))
            delete_task_command = DeleteTaskCommand(id)
            delete_task_command.execute(task_collection)

        elif command == "search":
            query = input("search: ")
            res = query_interpreter.interpret(query,task_collection)
            print("Search Results:")
            for re in res:
                print(f"{re.desc} - {re.state}")

        elif command == "show":
            task_collection.show_all_tasks()

        else:
            break

if __name__ == "__main__":
    main()