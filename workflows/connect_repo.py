from rich import print
from git_engine.git_checker import ensure_git_initialized
import subprocess


def connect_repository():
    """
    Workflow for connecting the current project to a GitHub repository.
    """

    print("[bold blue]Checking git status...[/bold blue]")

    ready = ensure_git_initialized()

    if not ready:
        print("[red]Cannot continue without git initialization[/red]")
        return

    # ask user for repository URL
    repo_url = input("Enter GitHub repository URL: ").strip()

    if not repo_url:
        print("[red]Repository URL not provided[/red]")
        return

    print("[yellow]Connecting remote repository...[/yellow]")

    try:
        # add remote origin
        subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)

        # ensure main branch
        subprocess.run(["git", "branch", "-M", "main"], check=True)

        print("[green]Repository connected successfully[/green]")

    except subprocess.CalledProcessError:
        print("[red]Remote may already exist or command failed[/red]")