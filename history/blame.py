import subprocess
import os
from rich import print
from InquirerPy import inquirer


def find_files_by_name(filename):
    """
    Search the entire project for files matching the given filename.
    """

    matches = []

    for root, dirs, files in os.walk("."):

        # skip .git directory
        if ".git" in root:
            continue

        if filename in files:
            full_path = os.path.join(root, filename)
            matches.append(full_path)

    return matches


def resolve_file_path():
    """
    Ask user for filename and resolve full path automatically.
    """

    filename = input("Enter file name (example: app.py): ").strip()

    if not filename:
        print("[red]Filename cannot be empty[/red]")
        return None

    matches = find_files_by_name(filename)

    if not matches:
        print("[red]No file found with that name[/red]")
        return None

    # only one match
    if len(matches) == 1:
        return matches[0]

    # multiple matches → let user choose
    print("[yellow]Multiple files found:[/yellow]")

    selected = inquirer.select(
        message="Select the file:",
        choices=matches
    ).execute()

    return selected


def check_file_history():
    """
    Show history for a file or specific line.
    """

    file_path = resolve_file_path()

    if not file_path:
        return

    line_number = input("Enter line number (press Enter to skip): ").strip()

    # specific line history
    if line_number:

        if not line_number.isdigit():
            print("[red]Invalid line number[/red]")
            return

        print("[yellow]Fetching line history...[/yellow]")

        result = subprocess.run(
            ["git", "blame", "-L", f"{line_number},{line_number}", file_path],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            print("[red]Failed to fetch history[/red]")
            print(result.stderr)
            return

        print("\n[green]Line History:[/green]")
        print(result.stdout)

    # whole file history
    else:

        print("[yellow]Fetching last file modification...[/yellow]")

        result = subprocess.run(
            ["git", "log", "-1", "--pretty=format:%h | %an | %ad | %s", file_path],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            print("[red]Failed to fetch history[/red]")
            print(result.stderr)
            return

        commit, author, date, message = result.stdout.split("|")

        print("\n[green]Last File Modification:[/green]")
        print(f"File   : {file_path}")
        print(f"Commit : {commit.strip()}")
        print(f"Author : {author.strip()}")
        print(f"Date   : {date.strip()}")
        print(f"Message: {message.strip()}")