import subprocess
from rich import print
from git_engine.git_checker import ensure_git_initialized


def create_branch():
    """
    Create a new git branch
    """

    # ensure git repo exists
    ready = ensure_git_initialized()

    if not ready:
        return

    branch_name = input("Enter new branch name: ").strip()

    if not branch_name:
        print("[red]Branch name cannot be empty[/red]")
        return

    print(f"[yellow]Creating branch '{branch_name}'...[/yellow]")

    result = subprocess.run(
        ["git", "checkout", "-b", branch_name],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("[red]Failed to create branch[/red]")
        print(result.stderr)
        return

    print(f"[green]Branch '{branch_name}' created and switched[/green]")
    
def merge_branch():
    """
    Merge another branch into current branch
    """

    ready = ensure_git_initialized()

    if not ready:
        return

    branch_name = input("Enter branch name to merge: ").strip()

    if not branch_name:
        print("[red]Branch name cannot be empty[/red]")
        return

    print(f"[yellow]Merging branch '{branch_name}'...[/yellow]")

    result = subprocess.run(
        ["git", "merge", branch_name],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("[red]Merge failed[/red]")
        print(result.stderr)
        return

    print("[green]Merge completed successfully[/green]")