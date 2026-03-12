import subprocess
from rich import print
from InquirerPy import inquirer


def get_branches():
    """
    Returns a list of local branches.
    """

    result = subprocess.run(
        ["git", "branch"],
        capture_output=True,
        text=True
    )

    branches = []

    for line in result.stdout.splitlines():
        branch = line.replace("*", "").strip()
        branches.append(branch)

    return branches


def choose_branch(message="Select a branch"):
    """
    Show branch selection menu.
    """

    branches = get_branches()

    if not branches:
        print("[red]No branches found[/red]")
        return None

    selected = inquirer.select(
        message=message,
        choices=branches
    ).execute()

    return selected