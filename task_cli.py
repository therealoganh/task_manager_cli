import click

from task_logic import add_task, list_tasks

@click.group()
def cli():
    """Task Manager CLI"""
    pass

# List CLI Command
@cli.command()
def list():
    """List all current tasks."""
    list_tasks()

@cli.command()
@click.argument('name')
@click.argument('duration', type=int)
def add(name, duration):
    """Add a new task with a name and duration (in hours)."""
    add_task(name, duration)
    click.echo(f"Task '{name}' added with duration {duration} hour(s)")


if __name__ == '__main__':
    cli()