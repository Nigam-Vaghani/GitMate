import subprocess


def get_commit_history(limit=10):
    """
    Return structured commit history.
    """

    result = subprocess.run(
        [
            "git",
            "log",
            f"-n{limit}",
            "--pretty=format:%h|%an|%ad|%s",
            "--date=short",
        ],
        capture_output=True,
        text=True
    )

    commits = []

    for line in result.stdout.splitlines():

        commit_hash, author, date, message = line.split("|", 3)

        files = subprocess.run(
            ["git", "show", "--name-only", "--pretty=format:", commit_hash],
            capture_output=True,
            text=True
        )

        file_list = [
            f.strip() for f in files.stdout.splitlines() if f.strip()
        ]

        commits.append({
            "hash": commit_hash,
            "author": author,
            "date": date,
            "message": message,
            "files": ", ".join(file_list)
        })

    return commits