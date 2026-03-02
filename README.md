# Sudoku Solver (numpy)

A simple Sudoku solver and checker implemented in Python using `numpy`. This repository contains a solver, basic I/O helpers, and utilities for running multiple runs and saving results.

**[中文文檔 (Traditional Chinese)](README_zh.md)**

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
python sudoku_solver.py
```

Follow the prompts to choose how many runs and whether to continue from the last run.

## Files

- `sudoku_solver.py`: Main solver and runner.
- `sudoku.txt`: Optional input puzzle (not tracked by git by default).
- `sudoku_results.txt`: Run outputs (ignored by git).

## License

Add a license file if you plan to publish this repository publicly (e.g., MIT).

---

For Chinese documentation see **[中文文檔 (Traditional Chinese)](README_zh.md)** .

## How it works

This project implements a simple Sudoku loader, validator and backtracking solver. Key components:

- `load_sudoku(file_path)`: reads a 9x9 whitespace-separated grid from `sudoku.txt`; if the file is missing, a random grid is generated.
- `generate_sudoku()`: produces a 9x9 grid filled with random integers 0–9 (0 means empty). Note: randomly generated puzzles are not guaranteed to be valid or solvable.
- `is_valid(grid, row, col, num)`: checks whether placing `num` in `(row, col)` breaks row, column, or 3x3-block constraints.
- `solve_sudoku(grid, errors)`: recursive backtracking solver that fills zero cells with valid candidates; `errors` is a 9x9 int matrix marking cells that had no valid candidate during search.
- `is_solvable(grid)`: deep-copies the grid, runs the solver and returns `(solvable, filled_grid, errors)`.
- `save_to_file(...)`: appends a human-readable record of each run to `sudoku_results.txt`.
- CLI `main(...)`: runs multiple puzzles (from file or random), prints puzzle & solution (or error map), and optionally appends results to the output file.

## Implementation details

- The solver uses plain backtracking (depth-first search). It attempts numbers 1–9 in empty cells and backtracks on conflicts. This is simple and reliable for typical puzzles but is not optimized for performance or uniqueness checking.
- `errors` is a helper matrix used to highlight positions where the solver found no candidate during a search path; it is not a formal proof of unsolvability for the whole puzzle.
- Output format in `sudoku_results.txt` is a textual line per run: `[run_number], [solvable], [original_grid], [solution_or_none]`. If you need machine-readable output, consider modifying `save_to_file` to write JSON.

## Notes & Caveats

- Input format: `sudoku.txt` must contain 9 lines with 9 integers each (0 for empty), separated by whitespace. Malformed files will cause the loader to raise a format error.
- Random puzzles from `generate_sudoku()` are likely to be invalid or have multiple conflicts — they are intended for quick manual testing only.
- Performance: backtracking is exponential in the worst case. For large numbers of runs or hard puzzles, consider adding heuristics (MRV, forward checking) or using a dedicated Sudoku library.
- Uniqueness: this solver finds a solution if one exists, but does not check whether the solution is unique.
- Colors and clear screen: the script uses ANSI color codes and `cls` for Windows. Some terminals may not render ANSI colors; remove color codes or use a cross-platform library if needed.
- Encoding: files are read with UTF-8; if you use a different encoding, update the `open` calls accordingly.

## Contributing

- If you'd like to improve the solver, consider:
  - Adding a constraint-propagation step (e.g., eliminate candidates before backtracking).
  - Implementing heuristics: choose the empty cell with fewest candidates (MRV), order candidate numbers, or use dancing links / exact cover for speed.
  - Changing `sudoku_results.txt` to JSON or CSV for easier analysis.
