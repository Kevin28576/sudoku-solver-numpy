# Sudoku Solver (numpy)
A simple Sudoku solver and checker implemented in Python using `numpy`. This repository contains a solver, basic I/O helpers, and utilities for running multiple runs and saving results. The primary README is in English; a Chinese README is provided in `README_zh.md`.

## Features
- Load a Sudoku puzzle from `sudoku.txt` or generate a random puzzle if the file is missing.
- Check solvability and attempt to solve the puzzle using a backtracking solver.
- Save run results to `sudoku_results.txt`.

## Requirements
- Python 3.8+
- See `requirements.txt` for Python package dependencies.

## Installation
1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

## Usage
1. Prepare a `sudoku.txt` file containing a 9x9 grid of integers (0 for empty cells), whitespace separated. If missing, the script will generate a random grid.
2. Run the solver:

```powershell
python 數獨.py
```

Follow the prompts to choose how many runs and whether to continue from the last run.

Output is appended to `sudoku_results.txt` by default. The `.gitignore` excludes temporary and result files and `bot.py` (personal script).

## Files
- `sudoku_solver.py`: Main solver and runner.
- `sudoku.txt`: Optional input puzzle (not tracked by git by default).
- `sudoku_results.txt`: Run outputs (ignored by git).
- `bot.py`: Personal script (excluded from repository uploads by `.gitignore`).

## License
Add a license file if you plan to publish this repository publicly (e.g., MIT).

---

For Chinese documentation see `README_zh.md`.