class Task:

    # initialize task class and properties
    def __init__(self, name, duration, isComplete):
        self.name = name
        self.duration = duration
        self.isComplete = isComplete

    # Format task object output
    def __str__(self):
        return f"Task: {self.name}, Duration: {self.duration} hours, Status: {'Complete' if self.isComplete == True else 'Incomplete'}"


# methods
# List tasks method
def list_tasks(lst):
    
    # Validate argument
    if (len(lst) == 0 or lst == None):
        print("The task list is currently empty. Try adding a task first!")
    else:
        print("=== Tasks ===")
        for task in lst:
            print(task)

# Task list
task_list = []

# Sample tasks
laundry = Task("Do the Laundry", 2, False)
dishes = Task("Do the dishes", 1, True)
task_list.append(laundry)
task_list.append(dishes)


def main():
    print("\nWelcome to Task Manager CLI!")
    print("============================")

    # Loop logic
    while True:
        print("1) List tasks")
        print("2) Add task")
        print("3) Complete task")
        print("4) Delete task")
        print("5) Exit")
        print("Select an option:", end=' ')
        menu_choice = int(input())

        # Menu selection logic
        if ((menu_choice < 1) or (menu_choice > 5)):
            print(f"\nInvalid input. Pick a valid menu option.\n")
            continue

        elif menu_choice == 1:
            print()
            list_tasks(task_list)
            print()
        elif menu_choice == 2:
            pass
        elif menu_choice == 3:
            pass
        elif menu_choice == 4:
            pass
        else:
            print("Goodbye!")
            return False
            


if __name__ == "__main__":
    main()
