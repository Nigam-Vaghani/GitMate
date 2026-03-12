import subprocess
from rich import print
from git_engine.git_checker import ensure_git_initialized
from utils.gitignore_manager import manage_gitignore
from git_engine.error_handler import interpret_git_error


def push_changes():
    """
    Workflow to push project changes to remote repository.
    """

    print("[bold blue]Preparing to push changes...[/bold blue]")

    # ensure git initialized
    ready = ensure_git_initialized()

    if not ready:
        print("[red]Cannot continue without git initialization[/red]")
        return

    # allow user to manage gitignore before commit
    manage_gitignore()

    # check git status
    status = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True,
        text=True
    )

    if not status.stdout.strip():
        print("[yellow]No changes detected[/yellow]")
        return

    print("[green]Changes detected[/green]")

    # show changed files
    print("\n[bold]Files changed:[/bold]")
    print(status.stdout)

    # ask commit message
    commit_message = input("\nEnter commit message: ").strip()

    if not commit_message:
        print("[red]Commit message cannot be empty[/red]")
        return

    print("[yellow]Adding files...[/yellow]")
    subprocess.run(["git", "add", "."])

    print("[yellow]Creating commit...[/yellow]")
    subprocess.run(["git", "commit", "-m", commit_message])

    print("[yellow]Pushing to remote...[/yellow]")
    result = subprocess.run(
        ["git", "push", "origin", "main"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        interpret_git_error(result.stderr)
        return

    print("[green]Push completed successfully[/green]")