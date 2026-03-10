from InquirerPy import inquirer
from rich import print
from workflows.connect_repo import connect_repository
from workflows.manage_gitignore import run_gitignore_manager
from workflows.push_changes import push_changes

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
                "merge branch",
                "Check file history",
                "Manage .gitignore",
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
        else:
            print("[yellow]Feature not implemented yet[/yellow]")
        