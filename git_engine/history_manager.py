import subprocess


def get_commit_history(limit=10):
    """
    Returns recent commit history including author.
    """

    result = subprocess.run(
        [
            "git",
            "log",
            f"-n{limit}",
            "--pretty=format:%h | %an | %s"
        ],
        capture_output=True,
        text=True
    )

    commits = result.stdout.splitlines()

    return commits