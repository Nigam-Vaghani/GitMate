import os
from rich import print
from InquirerPy import inquirer


def scan_root_items():
    """
    Scan root folder and return files + directories.
    """

    items = []

    for item in os.listdir("."):

        if item == ".git":
            continue

        # show directories clearly
        if os.path.isdir(item):
            items.append(item + "/")
        else:
            items.append(item)

    return items


def choose_gitignore_items(items):
    """
    Let user choose what to add to .gitignore
    """

    selected = inquirer.checkbox(
        message="Select files/folders to add to .gitignore:",
        choices=items
    ).execute()

    return selected


def update_gitignore(entries):

    if not entries:
        print("[yellow]No items selected for .gitignore[/yellow]")
        return

    with open(".gitignore", "a") as f:
        for entry in entries:
            f.write(entry + "\n")

    print("[green].gitignore updated successfully[/green]")

def manage_gitignore():
    """
    Main function to create or modify .gitignore
    """

    # check if file exists
    if not os.path.exists(".gitignore"):

        print("[yellow].gitignore not found[/yellow]")

        create = inquirer.confirm(
            message="Create .gitignore now?",
            default=True
        ).execute()

        if not create:
            return

        # create empty file
        open(".gitignore", "w").close()

        print("[green].gitignore created[/green]")

    else:
        print("[green].gitignore detected[/green]")

    # scan project
    items = scan_root_items()

    selected = choose_gitignore_items(items)

    update_gitignore(selected)