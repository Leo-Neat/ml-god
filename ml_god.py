


import subprocess
from datetime import datetime, timedelta
import calendar

# --- CONFIG ---
repo_path = None  # Use current working directory
author_name = "Leo Neat"
author_email = "leosneat@gmail.com"

# Define a grid for the letters (7x7 for each letter)
def transpose(grid):
    return [list(row) for row in zip(*grid)]

def reset_repo_history():
    # Remove all previous commits and start with a single initial commit
    subprocess.run(["git", "checkout", "--orphan", "temp-branch"], cwd=repo_path)
    subprocess.run(["git", "add", "-A"], cwd=repo_path)
    subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=repo_path)
    subprocess.run(["git", "branch", "-D", "main"], cwd=repo_path)
    subprocess.run(["git", "branch", "-m", "main"], cwd=repo_path)
    subprocess.run(["git", "push", "-f", "origin", "main"], cwd=repo_path)

letters = {
    "M": transpose([
        [10,0,0,0,0,0,10],
        [10,10,0,0,0,10,10],
        [10,0,10,0,10,0,10],
        [10,0,0,10,0,0,10],
        [10,0,0,0,0,0,10],
        [10,0,0,0,0,0,10],
        [10,0,0,0,0,0,10],
        [10,0,0,0,0,0,10],
    ]),
    "L": transpose([
        [10,0,0,0,0,0,0],
        [10,0,0,0,0,0,0],
        [10,0,0,0,0,0,0],
        [10,0,0,0,0,0,0],
        [10,0,0,0,0,0,0],
        [10,0,0,0,0,0,0],
        [10,10,10,10,10,0,0],
    ]),
    "G": transpose([
        [0,10,10,10,10,0,0],
        [10,0,0,0,0,0,0],
        [10,0,0,0,0,0,0],
        [10,0,0,10,10,10,0],
        [10,0,0,0,0,10,0],
        [10,0,0,0,0,10,0],
        [0,10,10,10,10,0,0],
    ]),
    "O": transpose([
        [0,10,10,10,0,0,0],
        [10,0,0,0,10,0,0],
        [10,0,0,0,10,0,0],
        [10,0,0,0,10,0,0],
        [10,0,0,0,10,0,0],
        [10,0,0,0,10,0,0],
        [0,10,10,10,0,0,0],
    ]),
    "D": transpose([
        [10,10,10,0,0,0,0],
        [10,0,0,10,0,0,0],
        [10,0,0,0,10,0,0],
        [10,0,0,0,10,0,0],
        [10,0,0,0,10,0,0],
        [10,0,0,10,0,0,0],
        [10,10,10,0,0,0,0],
    ]),
    " ": transpose([
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
    ]),
}
# Remove all previous commits before generating the pattern
reset_repo_history()

def make_commit(date):
    env = {
        "GIT_AUTHOR_NAME": author_name,
        "GIT_AUTHOR_EMAIL": author_email,
        "GIT_AUTHOR_DATE": date,
        "GIT_COMMITTER_NAME": author_name,
        "GIT_COMMITTER_EMAIL": author_email,
        "GIT_COMMITTER_DATE": date,
    }
    subprocess.run(["git", "commit", "--allow-empty", "-m", f"Commit for {date}"], cwd=repo_path, env=env)

# Calculate start date: 11 months ago from today, adjusted to previous Sunday
today = datetime.now()
eleven_months_ago = today.replace(day=1) - timedelta(days=1)  # go to last day of previous month
for _ in range(10):
    eleven_months_ago = eleven_months_ago.replace(day=1) - timedelta(days=1)
eleven_months_ago = eleven_months_ago.replace(day=today.day)
if eleven_months_ago > today:
    eleven_months_ago -= timedelta(days=calendar.monthrange(eleven_months_ago.year, eleven_months_ago.month)[1])

# Find previous Sunday
days_to_sunday = eleven_months_ago.weekday()  # Monday=0, Sunday=6
start_date = eleven_months_ago - timedelta(days=(days_to_sunday if days_to_sunday != 6 else 0))

for letter in "ML GOD":
    grid = letters[letter]
    for col_idx, column in enumerate(grid):
        for row_idx, cell in enumerate(column):
            if cell > 0:
                commit_date = start_date + timedelta(weeks=col_idx, days=row_idx) - timedelta(days=1)
                # Format Git date
                git_date = commit_date.strftime("%Y-%m-%d 12:00:00")
                for _ in range(cell):
                    make_commit(git_date)
    # Add 1 week spacing between letters
    start_date += timedelta(weeks=len(grid)+1)

print("Done! ")

# Push all generated commits to the remote repository and set upstream
subprocess.run(["git", "push", "--set-upstream", "origin", "main"], cwd=repo_path)
print("Pushed all commits to remote.")
