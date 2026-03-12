import subprocess
from rich import print
from git_engine.git_checker import ensure_git_initialized
from git_engine.branch_manager import choose_branch, get_branches
from InquirerPy import inquirer


def get_current_branch():

    result = subprocess.run(
        ["git", "branch", "--show-current"],
        capture_output=True,
        text=True
    )

    branch = result.stdout.strip()

    if not branch:
        return "detached HEAD"

    return branch


def create_branch():

    ready = ensure_git_initialized()

    if not ready:
        return

    branch_name = input("Enter new branch name: ").strip()

    if not branch_name:
        print("[red]Branch name cannot be empty[/red]")
        return

    print(f"[yellow]Creating branch '{branch_name}'...[/yellow]")

    result = subprocess.run(
        ["git", "switch", "-c", branch_name],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("[red]Failed to create branch[/red]")
        print(result.stderr)
        return

    print(f"[green]Branch '{branch_name}' created and switched[/green]")


def merge_branch():

    ready = ensure_git_initialized()

    if not ready:
        return

    current_branch = get_current_branch()

    branches = get_branches()

    branches = [b for b in branches if b != current_branch]

    if not branches:
        print("[yellow]No other branches available to merge[/yellow]")
        return

    branch_to_merge = inquirer.select(
        message=f"Current branch: {current_branch}\nSelect branch to merge:",
        choices=branches
    ).execute()

    confirm = inquirer.confirm(
        message=f"Merge '{branch_to_merge}' into '{current_branch}'?",
        default=True
    ).execute()

    if not confirm:
        print("[red]Merge cancelled[/red]")
        return

    print(f"[yellow]Merging '{branch_to_merge}' into '{current_branch}'...[/yellow]")

    result = subprocess.run(
        ["git", "merge", branch_to_merge],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("[red]Merge failed[/red]")
        print(result.stderr)
        return

    print("[green]Merge completed successfully[/green]")


def switch_branch():

    ready = ensure_git_initialized()

    if not ready:
        return

    branch_name = choose_branch("Select branch to switch")

    if not branch_name:
        return

    print(f"[yellow]Switching to '{branch_name}'...[/yellow]")

    result = subprocess.run(
        ["git", "switch", branch_name],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("[red]Failed to switch branch[/red]")
        print(result.stderr)
        return

    print(f"[green]Switched to '{branch_name}'[/green]")