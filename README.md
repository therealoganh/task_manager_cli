# Task Manager CLI

A Python-based command-line application to manage tasks, built using click for argument parsing and command routing. Demonstrates clean CLI design, persistent storage with SQLite, and modular code structure.

---

`tasks` is a collection of robust terminal commands that you can use to manipulate your 'task list' in various ways.

| Command  | Description | Example |
| ------------- | ------------- | ------------ |
| add  | Add a task to the database  | `tasks add "Start database project" 1` |
|  list | List all tasks in the database. Uses additonal parameters to filter results.  | `tasks list --complete` |
| complete  | Mark a task as 'Complete' using its task number.  | `tasks complete 7` |
| update  | Update a task's information, like name, duration, and status.  | `tasks update --name "Fix typos" --duration 1` |
| delete  | Delete a task using its task number.  | `tasks delete 5` |
