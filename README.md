# ml-god

This project creates a custom pattern in your GitHub contribution graph by making empty commits with specific dates. The pattern spells out "ML GOD" using a grid system, with each letter mapped to a series of commits.

## How It Works

- Each letter ("M", "L", "G", "O", "D") is represented as a 7x7 grid.
- The script iterates through each grid, and for every cell marked as `1`, it makes an empty commit on a calculated date.
- The commit dates are set so that the contribution graph displays the letters "ML GOD".
- Author name and email are set in the commit environment.

## Usage

1. Clone the repository.
2. Adjust the `repo_path`, `author_name`, and `author_email` variables in `ml_god.py` if needed.
3. Run the script:
   ```bash
   python3 ml_god.py
   ```
4. Push the commits to GitHub:
   ```bash
   git push origin main
   ```
5. View your GitHub contribution graph to see the pattern.

## Requirements

- Python 3.x
- Git installed and configured

## Disclaimer

This script makes a large number of empty commits. Use responsibly and consider cleaning up your commit history if needed.
