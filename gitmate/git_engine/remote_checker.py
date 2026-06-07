import subprocess
from rich import print
from InquirerPy import inquirer


def get_remote_url():
    """
    Returns the URL of the remote repository if it exists.
    Runs: git remote get-url origin
    """

    try:
        # run git command and capture output
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True,
            text=True
        )

        # if command succeeded, return the URL
        if result.returncode == 0:
            return result.stdout.strip()

        return None

    except Exception:
        return None


def ensure_remote_connected():
    """
    Checks if a remote repository is connected.
    If not, ask user to provide repository URL.
    """

    remote_url = get_remote_url()

    if remote_url:
        print("[green]Remote repository already connected[/green]")
        print(f"[cyan]origin → {remote_url}[/cyan]")
        return remote_url

    print("[yellow]No remote repository connected[/yellow]")

    print(
        "[bold]If you don't have a repository yet, create one here:[/bold]\n"
        "https://github.com/new"
    )

    repo_url = inquirer.text(
        message="Enter GitHub repository URL:"
    ).execute()

    return repo_url