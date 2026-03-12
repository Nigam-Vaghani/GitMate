# GitMate

GitMate is an interactive CLI assistant that simplifies Git workflows by guiding developers through common Git operations using a clean terminal interface.

Instead of remembering complex Git commands, GitMate provides a guided menu-based system that helps developers perform Git operations safely and efficiently.

---

## Why GitMate?

Git is extremely powerful but often confusing, especially for beginners.

Common problems developers face:

- Forgetting Git commands
- Pushing to the wrong branch
- Merge conflicts without clear guidance
- Managing `.gitignore` files
- Understanding commit history
- Checking who changed a specific line of code

GitMate solves these problems by acting as a **guided Git assistant directly inside the terminal**.

It reduces mistakes and helps developers focus on coding instead of remembering commands.

---

## Key Features

### Interactive CLI Menu
Navigate through Git operations using arrow keys.


---

### Connect Project to GitHub
GitMate helps initialize and connect repositories safely.


---

### Push Changes
Guided commit and push workflow:

- Detects changed files
- Allows `.gitignore` management
- Prompts for commit message
- Pushes current branch automatically

---

### Pull Changes (Safe Pull)

Before pulling, GitMate checks for uncommitted changes.


This prevents common merge errors.

---

### Branch Management

GitMate simplifies branch operations:

- Create branch
- Switch branch
- Merge branch

Branches can be selected interactively without typing names manually.

---

### `.gitignore` Manager

GitMate helps manage `.gitignore` interactively.

It scans project folders and lets you select files/folders to ignore.



---

### File History (Git Blame Simplified)

Find who last modified a specific line or file.


---

## Technologies Used

- Python
- InquirerPy (interactive CLI)
- Rich (terminal UI)
- Git CLI integration
- Subprocess automation

---

## Future Improvements

Planned features include:

- Natural language Git commands
- Repository health analyzer
- Automated Git suggestions
- Installable CLI command (`gitmate`)

---

## Author

**Nigam Vaghani**

Built as a developer productivity tool to simplify Git workflows and reduce command-line friction.