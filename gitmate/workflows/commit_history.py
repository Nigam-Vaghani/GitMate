from rich.console import Console
from rich.table import Table
from InquirerPy import inquirer
import subprocess

from gitmate.git_engine.history_manager import get_commit_history

console = Console()


def show_commit_history():

    commits = get_commit_history()

    if not commits:
        console.print("[red]No commits found[/red]")
        return

    table = Table(title="GitMate Commit History")

    table.add_column("Index", style="cyan")
    table.add_column("Author", style="green")
    table.add_column("Date", style="yellow")
    table.add_column("Message", style="white")
    table.add_column("Files Changed", style="magenta")

    for i, commit in enumerate(commits):
        table.add_row(
            str(i),
            commit["author"],
            commit["date"],
            commit["message"],
            commit["files"]
        )

    console.print(table)

    
    