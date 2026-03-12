from InquirerPy import inquirer
from rich import print
from workflows.connect_repo import connect_repository
from workflows.manage_gitignore import run_gitignore_manager
from workflows.push_changes import push_changes
from history.blame import check_file_history
from workflows.branch import create_branch, merge_branch, switch_branch


def show_main_menu():
    """
    Display the main GitMate menu
    """
    while True:
        actions = inquirer.select(
            message="- GitMate - ",
            choices=[
                "Connect project to GitHub",
                "Push changes",
                "Pull latest changes",
                "Create branch",
                "Merge branch",
                "Check file history",
                "Manage .gitignore",
                "Switch branch",
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
        else:
            print("[yellow]Feature not implemented yet[/yellow]")
        