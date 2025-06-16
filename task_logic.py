import sqlite3

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