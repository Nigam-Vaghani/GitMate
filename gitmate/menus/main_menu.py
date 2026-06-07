from InquirerPy import inquirer
from rich import print
from gitmate.workflows.connect_repo import connect_repository
from gitmate.workflows.manage_gitignore import run_gitignore_manager
from gitmate.workflows.push_changes import push_changes
from gitmate.history.blame import check_file_history
from gitmate.workflows.branch import create_branch, merge_branch, switch_branch
from gitmate.workflows.pull_chnages import pull_changes
from gitmate.workflows.status_dashboard import show_status_dashboard
from gitmate.workflows.commit_history import show_commit_history
from gitmate.workflows.branch import create_branch, merge_branch, switch_branch


def show_main_menu():
    """
    ok that works
    Display the main GitMate menu
    """
    while True:
        actions = inquirer.select(
            message="- GitMate - ",
            choices=[
                "Connect project to GitHub",
                "Repo status",
                "Push changes",
                "Pull latest changes",
                "Create branch",
                "Merge branch",
                "Switch branch",
                "Check file history",
                "Manage .gitignore",
                "Commit history",
                "Exit"
                
            ],
        ).execute()
            
        print(f"[bold green]Selected:[/bold green] {actions}")
        if actions == "Connect project to GitHub":
            connect_repository()
            
        elif actions == "Exit":
            print("[bold red]Exiting GitMate...[/bold red]")
            break  
        elif actions == "Manage .gitignore":
            run_gitignore_manager()
        elif actions == "Push changes":
            push_changes()
        elif actions == "Check file history":
            check_file_history()
        elif actions == "Create branch":
            create_branch()
        elif actions == "merge branch":
            merge_branch()
        elif actions == "Switch branch":
            switch_branch()
        elif actions == "Pull latest changes":
            pull_changes()
        elif actions == "Repo status":
            show_status_dashboard()
        elif actions == "Commit history":
            show_commit_history()
        elif actions == "Merge branch":
            merge_branch()
        else:
            print("[yellow]Feature not implemented yet[/yellow]")
        