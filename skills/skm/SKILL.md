# Skill Manager (skm)

**Description:** Manage local custom skills and sync them with a git repository (`openclaw-skills`). Use this to "adopt" local skills into version control or push updates.

## Usage

Run the `skm` command from the workspace root.

### Commands

*   `./skm status`: Show the status of the `openclaw-skills` git repo.
*   `./skm adopt <skill_name>`: Move a local skill from `skills/<name>` into the git repo and create a symlink back. Use this to start tracking a new custom skill.
*   `./skm push "<message>"`: Commit all changes in the `openclaw-skills` repo and push to GitHub.
*   `./skm pull`: Pull latest changes from GitHub.

## Workflow

1.  **Create:** Create a new folder `skills/my-new-skill`.
2.  **Develop:** Write `SKILL.md` and any scripts.
3.  **Adopt:** Run `./skm adopt my-new-skill`.
4.  **Sync:** Run `./skm push "Initial commit"`.

## Directory Structure

*   `~/workspace/skm`: Wrapper script.
*   `~/workspace/skills/skm/skm.py`: The logic.
*   `~/workspace/openclaw-skills/`: The git repository.
*   `~/workspace/skills/`: Contains symlinks to the repo.
