import click

from task_logic import add_task, delete_task, list_tasks, mark_complete

@click.group()
def cli():
    """Task Manager CLI"""
    pass

# List CLI Command
@cli.command()
def list():
    """List all current tasks."""
    list_tasks()

# Add CLI command
@cli.command()
@click.argument('name')
@click.argument('duration', type=int)
def add(name, duration):
    """Add a new task with a name and duration (in hours)."""
    add_task(name, duration)
    click.echo(f"Task '{name}' added with duration {duration} hour(s)")

# Complete CLI command
@cli.command()
@click.argument('task_number', type=int)
def complete(task_number):
    """Mark a task as 'Complete' using its task number from the list."""
    id_map = list_tasks()

    if task_number in id_map:
        task_id = id_map[task_number]
        mark_complete(task_id)
        click.echo(f"Task {task_number} marked complete.")
    else:
        click.echo("Invalid task number.")

# Deletge CLI command
@cli.command()
@click.argument('task_number', type=int)
def delete(task_number):
    """Delete a task using its task number from the list."""
    id_map = list_tasks()

    if task_number in id_map:
        task_id = id_map[task_number]
        delete_task(task_id)
        click.echo(f"Task {task_number} deleted.")
    else:
        click.echo("Invalid task number.")

if __name__ == '__main__':
    cli()