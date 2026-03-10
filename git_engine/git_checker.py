import os
from rich import print
from InquirerPy import inquirer
import subprocess


def is_git_repository():
    """
    Check if current directory is a Git repository
    by verifying the presence of the .git folder
    """
    return os.path.isdir(".git")


def check_git_status():
    """
    Print git initialization status for current project
    """
    if is_git_repository():
        print("[green]Git repository detected[/green]")
    else:
        print("[red]Git is NOT initialized in this folder[/red]")


def initialize_git():
    # show message before running git init
    print("[yellow]Initializing git repository...[/yellow]")

    # execute git init command
    subprocess.run(["git", "init"])

    # success message
    print("[green]Git repository initialized successfully[/green]")


def ensure_git_initialized():
    """
    Ensures that the project has Git initialized.
    If not, ask the user whether to initialize it.
    """

    if is_git_repository():
        print("[green]Git repository detected[/green]")
        return True

    print("[red]Git is not initialized in this project[/red]")

    init_choice = inquirer.confirm(
        message="Run git init now?",
        default=True
    ).execute()

    if init_choice:
        initialize_git()
        return True
    else:
        print("[yellow]Git initialization skipped[/yellow]")
        return False