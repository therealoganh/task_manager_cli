import click

from task_logic import add_task, delete_task, list_tasks, mark_complete, update_task

@click.group()
def cli():
    """Task Manager CLI"""
    pass

# List CLI Command
@cli.command()
@click.option('--complete', is_flag=True, help="Show only completed tasks.")
@click.option('--incomplete', is_flag=True, help="Show only incomplete tasks.")
def list(complete, incomplete):
    """List all current tasks."""
    if complete and incomplete:
        click.echo("You can't use both --complete and --incomplete at the same time.")
        return
    
    status_filter = None
    if complete:
        status_filter = 1
    elif incomplete:
        status_filter = 0

    list_tasks(status_filter)

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
    id_map = list_tasks(suppress_output = True)

    if task_number in id_map:
        task_id = id_map[task_number]
        mark_complete(task_id)
        click.echo(f"\nTask {task_number} marked complete.")
        list_tasks() # Shows complete output
        print()
    else:
        click.echo("Invalid task number.")

# Delete CLI command
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

# Update CLI command
@cli.command()
@click.argument('task_number', type=int)
@click.option('--name', type=str, help="New name for the task.")
@click.option('--duration', type=int, help="New duration for the task (in hours).")
def update(task_number, name, duration):
    if not name and duration is None:
        click.echo("You must provide --name and/or --duration to update.")
        return
    
    id_map = list_tasks(suppress_output=True)

    if task_number in id_map:
        task_id = id_map[task_number]
        update_task(task_id, name, duration)
        click.echo(f"Task {task_number} updated.\n")
        list_tasks()

    else:
        click.echo("Invalid task number.")

if __name__ == '__main__':
    cli()