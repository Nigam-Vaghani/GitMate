from rich import print
from InquirerPy import inquirer
import subprocess

from git_engine.history_manager import get_commit_history


def show_commit_history():
    """
    Show interactive commit history.
    """

    commits = get_commit_history()

    if not commits:
        print("[red]No commits found[/red]")
        return

    selected = inquirer.select(
        message="Select a commit to inspect:",
        choices=commits
    ).execute()

    commit_hash = selected.split("|")[0].strip()

    print("\n[bold cyan]Commit Details[/bold cyan]\n")

    result = subprocess.run(
        ["git", "show", commit_hash],
        capture_output=True,
        text=True
    )

    print(result.stdout)