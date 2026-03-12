import subprocess


def has_uncommitted_changes():
    """
    Check if the working tree has uncommitted changes.
    """

    result = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True,
        text=True
    )

    return bool(result.stdout.strip())