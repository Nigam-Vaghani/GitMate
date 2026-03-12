from rich import print


def interpret_git_error(error_message):
    """
    Interpret common Git errors and show helpful suggestions.
    """

    error_message = error_message.lower()

    # repository not found
    if "repository not found" in error_message:
        print("[red]Error: Repository not found[/red]\n")

        print("[bold]Possible reasons:[/bold]")
        print("• Repository URL is incorrect")
        print("• Repository does not exist")
        print("• You do not have access permission\n")

        print("[bold]Suggestions:[/bold]")
        print("✔ Verify the repository URL")
        print("✔ Check GitHub permissions")
        print("✔ Ensure repository exists")

    # authentication error
    elif "authentication failed" in error_message:
        print("[red]Authentication failed[/red]\n")

        print("[bold]Possible reasons:[/bold]")
        print("• Incorrect credentials")
        print("• GitHub token expired")
        print("• SSH key not configured\n")

        print("[bold]Suggestions:[/bold]")
        print("✔ Use a valid GitHub token")
        print("✔ Configure SSH keys")

    # remote already exists
    elif "remote origin already exists" in error_message:
        print("[yellow]Remote 'origin' already exists[/yellow]\n")

        print("[bold]Suggestion:[/bold]")
        print("✔ Use 'git remote set-url origin <url>' instead")

    # default fallback
    else:
        print("[red]Git Error:[/red]")
        print(error_message)