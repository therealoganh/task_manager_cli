class Task:

    # initialize task class and properties
    def __init__(self, name, duration, isComplete):
        self.name = name
        self.duration = duration
        self.isComplete = isComplete

    # Format task object output
    def __str__(self):
        return f"Task: {self.name}, Duration: {self.duration}, Status {"Complete" if self.isComplete == True else "Incomplete"}"


# methods
# List tasks method
def list_tasks(lst):
    
    # Validate argument
    if (len(lst) == 0 or lst == None):
        

# Task list
task_list = []

# Sample tasks
laundry = Task("Do the Laundry", 2, False)
dishes = Task("Do the dishes", 1, True)
task_list.append(laundry)
task_list.append(dishes)


def main():
    print("Welcome to Task Manager CLI!")
    print("============================")
    
    print("Choose a menu option to get started:")

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








if __name__ == "__main__":
    main()
