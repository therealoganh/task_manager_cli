import sqlite3

# Database Methods
def init_db():
    print("Initializing database...")
    conn = sqlite3.connect("tasks.sqlite3") # Creates the DB file if it does not exist
    cursor = conn.cursor()

    # Executes sql w/ cursor
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            duration INTEGER,
            is_complete INTEGER DEFAULT 0
        )
    """)

    # Commits and releases file
    conn.commit()
    conn.close()

# Menu Methods
# ------------------------------

# Add Task Method
def add_task(name, duration):
    conn = sqlite3.connect("tasks.sqlite3")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tasks (name, duration, is_complete)
        VALUES (?, ?, 0)
    """, (name, duration))

    conn.commit()
    conn.close()

# List Tasks Method
def list_tasks():
    conn = sqlite3.connect("tasks.sqlite3")
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, duration, is_complete FROM tasks")
    tasks = cursor.fetchall()
    
    conn.close()

    # Check if no tasks exist
    if not tasks:
        print("\nThe task list is currently empty. Try adding a task first!")
        return {}
    
    id_map = {}
    
    print("\n=== Tasks ===")
    for i, task in enumerate(tasks, start=1):
        task_id, name, duration, is_complete = task
        status = "Complete" if is_complete == 1 else "Incomplete"
        print(f"{i}. {name} — {duration} hour(s) — {status}")
        id_map[i] = task_id  # Store mapping from display index to database ID

    return id_map

# Mark a task complete Method
def mark_complete(id):
    conn = sqlite3.connect("tasks.sqlite3")
    cursor = conn.cursor()

    cursor.execute("UPDATE tasks SET is_complete = 1 WHERE id = ?", (id,))

    conn.commit()
    conn.close()

# Delete a task Method
def delete_task(id):

    conn = sqlite3.connect("tasks.sqlite3")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))

    conn.commit()
    conn.close()


# MAIN PROGRAM
def main():
    init_db()
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
            list_tasks()
            print()

        elif menu_choice == 2:
            print("\nEnter task name:", end=' ')
            name = input()
            
            print("Enter estimated duration (in hours):", end=' ')
            try:
                duration = int(input())
            except ValueError:
                print("Invalid input. Duration must be a number.\n")
                return
            
            add_task(name, duration)
            print(f"\nTask '{name}' added successfully!\n")

        elif menu_choice == 3:
            id_map = list_tasks()

            if not id_map:
                continue

            try:
                print("\nEnter the task number you'd like to mark complete (or 0 to cancel): ", end=' ')
                choice = int(input())

                if choice == 0:
                    print("\nCanceled.\n")
                elif choice in id_map:
                    real_id = id_map[choice]
                    mark_complete(real_id)
                    print(f"Task {choice} was marked complete.\n")
                else:
                    print("Invalid task number.\n")
            except ValueError:
                print("\nInvalid input. Please enter a number.\n")

        elif menu_choice == 4:
            id_map = list_tasks()

            if not id_map:
                continue

            try:
                print("\nEnter the task number you'd like to delete (or 0 to cancel):", end=' ')
                choice = int(input())

                if choice == 0:
                    print("\nCanceled.\n")
                elif choice in id_map:
                    real_id = id_map[choice]
                    delete_task(real_id)
                    print(f"Task {choice} deleted.\n")
                else:
                    print("Invalid task number.\n")

            except ValueError:
                print("Invalid input. Please enter a number.\n")

        else:
            print("\nGoodbye!\n")
            return False
            


if __name__ == "__main__":
    main()
