# GitMate

GitMate is a menu-driven Git assistant for developers who work in the terminal and want fewer Git mistakes during daily work.

It wraps common Git operations in guided workflows so you can move faster without memorizing every command or flag.

## Tools and Technologies

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-CLI-F05032?style=for-the-badge&logo=git&logoColor=white)
![Rich](https://img.shields.io/badge/Rich-Terminal%20UI-FAFAFA?style=for-the-badge&logo=python&logoColor=3776AB)
![InquirerPy](https://img.shields.io/badge/InquirerPy-Interactive%20Prompts-2E8B57?style=for-the-badge&logo=readthedocs&logoColor=white)
![GitPython](https://img.shields.io/badge/GitPython-3.1.46-4B8BBE?style=for-the-badge&logo=python&logoColor=white)
![Typer](https://img.shields.io/badge/Typer-CLI%20Framework-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Click](https://img.shields.io/badge/Click-CLI%20Utilities-1F6FEB?style=for-the-badge&logo=python&logoColor=white)
![Prompt Toolkit](https://img.shields.io/badge/Prompt__Toolkit-Terminal%20Input-6A5ACD?style=for-the-badge&logo=gnometerminal&logoColor=white)
![Pygments](https://img.shields.io/badge/Pygments-Syntax%20Highlighting-FFB000?style=for-the-badge&logo=python&logoColor=white)
![Setuptools](https://img.shields.io/badge/Setuptools-Packaging-2C3E50?style=for-the-badge&logo=pypi&logoColor=white)

## The Problem GitMate Solves

Most developers do not struggle with Git fundamentals. They struggle with Git context-switching.

During a normal workday, small Git tasks interrupt coding flow:

- "I just want to push, but first I need to check what changed."
- "I need to pull, but I forgot I have local edits."
- "I want to switch branches safely without typing names wrong."
- "I need quick file history without building a long blame command."
- "I keep postponing .gitignore cleanup until it becomes noisy."

GitMate is built for exactly this layer of day-to-day friction.

## How GitMate Helps in Real Daily Workflow

GitMate gives you one interactive entry point and guides you through the steps that are usually easy to forget under pressure.

### 1) Start from menu, not memory

You choose the task from a clear CLI menu instead of recalling commands from memory.

### 2) Safe push path

The push workflow:

- ensures Git is initialized
- allows .gitignore update before commit
- shows changed files
- asks for a commit message
- pushes current branch to origin

### 3) Safer pull behavior

Before pulling, GitMate checks for uncommitted changes and gives you options:

- commit changes
- stash changes
- cancel pull

This avoids the classic "I pulled with dirty working tree" headache.

### 4) Branch operations with less risk

Create, switch, and merge branches through guided selections, reducing typo-driven mistakes.

### 5) Quick history lookup

Check last modification of a file or inspect a specific line with guided prompts.

## Feature Set

- Interactive main menu for core Git actions
- Connect local project to remote GitHub repository
- Repository status dashboard (branch, modified/untracked files, ahead/behind summary)
- Push workflow with change review and commit prompt
- Pull workflow with uncommitted-change handling
- Branch create, switch, and merge workflows
- Commit history table with files changed
- File or line-level history lookup
- Interactive .gitignore manager

## Project Structure

Core modules are organized by responsibility:

- `gitmate/menus`: main CLI entry menu
- `gitmate/workflows`: user-facing workflows (push, pull, branch, status, connect)
- `gitmate/git_engine`: low-level Git checks and utility operations
- `gitmate/history`: file/line history helpers
- `gitmate/utils`: utility helpers such as .gitignore management

## Installation

### Prerequisites

- Python 3.9+
- Git installed and available in PATH

### Option A: Install in editable mode (recommended for contributors)

```bash
pip install -e .
```

### Option B: Install dependencies only

```bash
pip install -r requirements.txt
```

## Usage

If installed with console script:

```bash
gitmate
```

Or run directly with Python:

```bash
python -m gitmate.cli
```

## Typical Developer Scenarios

### Scenario: End-of-day push without missing files

Use `Push changes` in GitMate:

1. review changed files
2. update `.gitignore` if needed
3. add commit message
4. push current branch

### Scenario: Pull latest code while you have local edits

Use `Pull latest changes` in GitMate:

1. GitMate detects uncommitted changes
2. choose commit, stash, or cancel
3. pull from origin for current branch

### Scenario: Validate branch state before standup/demo

Use `Repo status` and `Commit history` to quickly inspect branch state and recent changes.

## Current Limitations

- Designed for interactive local terminal usage (not non-interactive scripts)
- Uses Git CLI subprocess calls; behavior depends on local Git configuration
- Error handling covers common cases, but some edge cases still need refinement
- No license file is included yet

## Roadmap

- Stronger validation and guardrails around remote operations
- Better conflict-resolution guidance during merges/pulls
- Expanded status insights and repository diagnostics
- Test coverage and CI pipeline setup
- Packaging and release hardening for broader distribution

## Contributing

Contributions are welcome.

If you want to improve GitMate:

1. fork the repository
2. create a feature branch
3. implement and test your changes
4. open a pull request with a clear description

## Author

Nigam Vaghani

Built to reduce Git friction in everyday development and make common workflows safer and faster.