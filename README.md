### *AI written text below*

# Git Reference Guide
**Git** is a distributed version control system designed to track changes in source code during software development. It allows multiple developers to work together smoothly without overwriting each other's changes.

## 🚀 Getting Started
Before using Git, configure your identity so your commits are properly attributed.

```bash
# Set your global username
git config --global user.name "Your Name"

# Set your global email address
git config --global user.email "youremail@example.com"
```

## 📁 Starting a Repository
To begin tracking a project, you must either create a new repository or download an existing one.

```bash
# Initialize a local Git repository in the current folder
git init

# Clone (download) a remote repository from GitHub/GitLab
git clone <repository-url>
```

## 🛠️ The Daily Workflow
The standard Git workflow follows a three-step cycle: **Modify files ➡️ Stage changes ➡️ Commit snapshots**.

```bash
# Check the status of your files (untracked, modified, staged)
git status

# Add a specific file to the staging area
git add <file-name>

# Add ALL modified and untracked files to staging
git add .

# Save your staged snapshot to project history with a descriptive message
git commit -m "Describe the changes you made"
```

## 🌿 Managing Branches
Branches isolate your work-in-progress features so you don't break the main source code.

```bash
# List all local branches (current branch has an asterisk *)
git branch

# Create a new branch
git branch <branch-name>

# Switch to a specific branch
git checkout <branch-name>

# Shortcut: Create AND switch to a new branch instantly
git checkout -b <branch-name>

# Merge another branch's changes into your current active branch
git merge <branch-name>

# Delete a branch once it is no longer needed
git branch -d <branch-name>
```

## ☁️ Remote Synchronization
To collaborate with others, sync your local project history with online servers like GitHub.

```bash
# Download updates and merge them into your current local branch
git pull

# Upload your local commits to the remote online repository
git push origin <branch-name>

# View connected remote repository links
git remote -v
```

## ⏪ Undoing Changes
If you make a mistake, Git provides safety nets to revert or inspect past changes.

```bash
# View your project's commit history logs
git log --oneline

# Unstage a file but keep its current text modifications
git reset <file-name>

# Revert a file back to its state at the last commit (discard local edits)
git checkout -- <file-name>
```
