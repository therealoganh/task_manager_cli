import sqlite3

# List Tasks Method
def list_tasks(status_filter=None, suppress_output=False):
    conn = sqlite3.connect("tasks.sqlite3")
    cursor = conn.cursor()

    # Status filter logic
    if status_filter == None:
        cursor.execute("SELECT id, name, duration, is_complete FROM tasks")
    else:
        cursor.execute("""
            SELECT id, duration, is_complete
            FROM tasks
            WHERE is_complete = ?
                       """, (status_filter,))
        
    tasks = cursor.fetchall()
    conn.close()

    # Check if no tasks exist
    if not tasks:
        if not suppress_output:
            print("\nNo matching tasks found.")
        return {}
    
    id_map = {}
    
    if not suppress_output:
        print("\n=== Tasks ===")
        for i, task in enumerate(tasks, start=1):
            task_id, name, duration, is_complete = task
            status = "Complete" if is_complete == 1 else "Incomplete"
            print(f"{i}. {name} — {duration} hour(s) — {status}")
            id_map[i] = task_id  # Store mapping from display index to database ID

    for i, task in enumerate(tasks, start=1):
        task_id, *_ = task
        id_map[i] = task_id
    
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

# Update a task method
def update_task(task_id, name=None, duration=None):
    conn = sqlite3.connect("tasks.sqlite3")
    cursor = conn.cursor()

    if name is not None and duration is not None:
        cursor.execute("""
            UPDATE tasks
            SET name = ?, duration = ?
            WHERE id = ?
        """, (name, duration, task_id))

    elif name is not None:
        cursor.execute("""
            UPDATE tasks
            SET name = ?
            WHERE id = ?
        """, (name, task_id))

    elif duration is not None:
        cursor.execute("""
            UPDATE tasks
            SET duration = ?
            WHERE id = ?
        """, (duration, task_id))

    conn.commit()
    conn.close()