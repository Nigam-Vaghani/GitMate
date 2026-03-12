import subprocess
from rich import print
from InquirerPy import inquirer

from git_engine.git_checker import ensure_git_initialized
from git_engine.error_handler import interpret_git_error
from git_engine.working_tree import has_uncommitted_changes


def get_current_branch():

    result = subprocess.run(
        ["git", "branch", "--show-current"],
        capture_output=True,
        text=True
    )

    return result.stdout.strip()


def pull_changes():

    print("[bold blue]Preparing to pull latest changes...[/bold blue]")

    ready = ensure_git_initialized()

    if not ready:
        return

    # NEW: check working tree state
    if has_uncommitted_changes():

        print("[yellow]You have uncommitted changes[/yellow]")

        action = inquirer.select(
            message="How would you like to proceed?",
            choices=[
                "Commit changes",
                "Stash changes",
                "Cancel pull"
            ]
        ).execute()

        if action == "Commit changes":

            subprocess.run(["git", "add", "."])
            message = input("Enter commit message: ")
            subprocess.run(["git", "commit", "-m", message])

        elif action == "Stash changes":

            subprocess.run(["git", "stash"])

        else:
            print("[red]Pull cancelled[/red]")
            return

    branch = get_current_branch()

    if not branch:
        print("[red]Could not detect current branch[/red]")
        return

    print(f"[yellow]Pulling latest changes for '{branch}'...[/yellow]")

    result = subprocess.run(
        ["git", "pull", "origin", branch],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        interpret_git_error(result.stderr)
        return

    print("[green]Pull completed successfully[/green]")