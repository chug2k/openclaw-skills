#!/usr/bin/env python3
import os
import sys
import subprocess
import shutil

REPO_DIR = os.path.abspath("openclaw-skills")
SKILLS_DIR = os.path.abspath("skills")

def run(cmd, cwd=None):
    try:
        subprocess.check_call(cmd, shell=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        print(f"Error running: {cmd}")
        sys.exit(e.returncode)

def status():
    print(f"--- Git Status ({REPO_DIR}) ---")
    run("git status -s", cwd=REPO_DIR)

def push(message):
    if not message:
        print("Error: Commit message required.")
        return
    run("git add .", cwd=REPO_DIR)
    run(f'git commit -m "{message}"', cwd=REPO_DIR)
    run("git push", cwd=REPO_DIR)
    print("✅ Pushed to GitHub.")

def pull():
    run("git pull", cwd=REPO_DIR)
    print("✅ Pulled from GitHub.")

def adopt(skill_name):
    """Moves a local skill to the repo and symlinks it back."""
    local_path = os.path.join(SKILLS_DIR, skill_name)
    repo_path = os.path.join(REPO_DIR, "skills", skill_name)

    if not os.path.exists(local_path):
        print(f"Error: Local skill '{skill_name}' not found.")
        return

    if os.path.islink(local_path):
        print(f"Skill '{skill_name}' is already symlinked.")
        return

    if os.path.exists(repo_path):
        print(f"Error: Skill '{skill_name}' already exists in the repo.")
        return

    print(f"📦 Moving {local_path} -> {repo_path}...")
    shutil.move(local_path, repo_path)
    
    print(f"🔗 Creating symlink...")
    os.symlink(os.path.relpath(repo_path, SKILLS_DIR), local_path)
    print(f"✅ Adopted '{skill_name}' into git tracking.")

def help():
    print("Usage: skill-sync [command]")
    print("  status          Show repo status")
    print("  pull            Pull latest changes")
    print("  push <msg>      Commit and push changes")
    print("  adopt <name>    Move a local skill into the repo and link it")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == "status":
        status()
    elif cmd == "push":
        push(sys.argv[2] if len(sys.argv) > 2 else "Update skills")
    elif cmd == "pull":
        pull()
    elif cmd == "adopt":
        adopt(sys.argv[2] if len(sys.argv) > 2 else None)
    else:
        help()
