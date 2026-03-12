from rich import print
from git_engine.status_checker import (
    get_current_branch,
    get_changes_summary,
    get_ahead_behind,
)


def show_status_dashboard():
    """
    Display repository status summary.
    """

    branch = get_current_branch()

    modified, untracked = get_changes_summary()

    ahead_behind = get_ahead_behind()

    print("\n[bold cyan]GitMate Repository Status[/bold cyan]\n")

    print(f"[green]Current Branch:[/green] {branch}")

    print(f"[yellow]Modified Files:[/yellow] {modified}")

    print(f"[yellow]Untracked Files:[/yellow] {untracked}")

    print(f"[blue]Git Status:[/blue] {ahead_behind}\n")