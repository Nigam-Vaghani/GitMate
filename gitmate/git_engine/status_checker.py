import subprocess


def get_current_branch():
    """
    Returns the currently active branch.
    """

    result = subprocess.run(
        ["git", "branch", "--show-current"],
        capture_output=True,
        text=True
    )

    return result.stdout.strip()


def get_changes_summary():
    """
    Returns number of modified and untracked files.
    """

    result = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True,
        text=True
    )

    modified = 0
    untracked = 0

    for line in result.stdout.splitlines():

        if line.startswith("??"):
            untracked += 1
        else:
            modified += 1

    return modified, untracked


def get_ahead_behind():
    """
    Detect commits ahead/behind remote.
    """

    result = subprocess.run(
        ["git", "status", "-sb"],
        capture_output=True,
        text=True
    )

    status_line = result.stdout.splitlines()[0]

    return status_line