import argparse
import os

TASK_FILE = ".tasks.txt"

def add_task(task):
    """Function: add_task
    
    Input - a task to add to the list
    Return - nothing
    """

def list_tasks():
    try:
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            tasks = file.readlines()
            counter = 1 
            output_string=""
        #iterate through all tasks except last
            for i in range(len(tasks)-1):
                task = tasks[i]
                output_string = output_string + str(counter) + ". " + task
                counter = counter + 1 
            return output_string
    except FileNotFoundError:
        return"No tasks found." 

def remove_task(index):
    try: 
        with open(TASK_FILE, "r", encoding="utf-8") as file: 
            tasks = file.readlines() 
            
        if 1 <= index <= len(tasks): 
            # Python index starts at 0 therefore - 1 to get correct position in list
            index_to_remove = index - 1 
            del tasks[index_to_remove]
            
            with open(TASK_FILE, "w", encoding="utf-8") as file: 
                counter = 1 
                for task in tasks: 
                    file.write(f"{counter}. {task.split('.', 1)[-1]}") # Assign number to next task 
                    counter += 1
        else: 
            pass 
        
    except FileNotFoundError:
        print(f"Error: Task file '{TASK_FILE}' not found.")
        
    TASK_FILE = ".tasks.txt"
                    
            
    return

def main():
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument(
            "-a",
            "--add",
            help="Add a new task"
            )
    parser.add_argument(
            "-l",
            "--list",
            action="store_true",
            help="List all tasks")
    parser.add_argument(
            "-r",
            "--remove",
            help="Remove a task by index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        tasks = list_tasks()
        print(tasks)
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
