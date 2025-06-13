import argparse

parser = argparse.ArgumentParser(description="Simple CLI TODO App")

parser.add_argument("command", choices=[
                    "add", "list"], help="Command to run: add or list")
parser.add_argument("task", nargs="?",
                    help="Task description (required for add)")

args = parser.parse_args()


def add_task(task):
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")
    print(f"Added task: {task}")


def list_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks file found yet.")


if args.command == "add":
    if not args.task:
        print("Please provide a task description.")
    else:
        add_task(args.task)
elif args.command == "list":
    list_tasks()
