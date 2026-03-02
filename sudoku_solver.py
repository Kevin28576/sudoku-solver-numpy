import numpy as np
import copy
import time
import random
import os
import re

clear = lambda: os.system('cls')

def generate_sudoku():
    grid = [[random.randint(0, 9) for _ in range(9)] for _ in range(9)]
    return grid


def load_sudoku(file_path):
    if not os.path.exists(file_path):
        print(f"No such file: {file_path}. Generating a random sudoku puzzle.")
        return generate_sudoku()
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            grid = [[int(num) for num in line.split()] for line in file]
        if len(grid) != 9 or any(len(row) != 9 for row in grid):
            raise ValueError("Sudoku format is incorrect. It should be a 9x9 grid.")
        return grid
    except ValueError as ve:
        print(ve)


def get_last_run_number(file_path):
    if not os.path.exists(file_path):
        return 0  # If file doesn't exist, start from 1
    with open(file_path, 'r') as file:
        lines = file.readlines()
        max_run_number = 0
        for line in lines:
            match = re.search(r"\[(\d+)\]", line)
            if match:
                run_number = int(match.group(1))
                max_run_number = max(max_run_number, run_number)
        return max_run_number


def save_to_file(run_number, is_solvable, grid, solution, file_path, mode='a'):
    with open(file_path, mode) as file:
        solvable_str = "solvable" if is_solvable else "unsolvable"
        file.write(f"[{run_number}], [{solvable_str}], {grid}, {solution}\n")


def is_valid(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True


def solve_sudoku(grid, errors):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                valid_nums = [num for num in range(1, 10) if is_valid(grid, row, col, num)]
                if not valid_nums:
                    errors[row][col] = 1
                for num in valid_nums:
                    grid[row][col] = num
                    if solve_sudoku(grid, errors):
                        return True
                    grid[row][col] = 0
                return False
    return True


def is_solvable(grid):
    temp_grid = copy.deepcopy(grid)
    errors = np.zeros((9, 9), dtype=int)
    solvable = solve_sudoku(temp_grid, errors)
    return solvable, temp_grid, errors


def print_sudoku_with_errors(grid, errors):
    for i, row in enumerate(grid):
        if i % 3 == 0 and i != 0:
            print("- - - + - - - + - - -")
        for j, num in enumerate(row):
            num_str = str(num) if num != 0 else f"\033[37m.\033[0m"
            if errors[i][j] == 1:
                print(f"\033[91mX\033[0m", end=" ")
            else:
                print(f"\033[36m{num_str}\033[0m", end=" ")
            if j == 2 or j == 5:
                print("|", end=" ")
        print()


def print_sudoku(grid, title="Sudoku"):
    print(title + ":")
    print(grid)  # Matrix form
    print("\n給人看的:")
    for i, row in enumerate(grid):
        if i % 3 == 0 and i != 0:
            print("- - - + - - - + - - -")
        for j, num in enumerate(row):
            num_str = str(num) if num != 0 else f"\033[37m.\033[0m"
            print(f"\033[32m{num_str}\033[0m", end=" ")
            if j == 2 or j == 5:
                print("|", end=" ")
        print()
    print()

def print_sudoku_q(grid, title="Sudoku"):
    print(title + ":")
    print(grid)  # Matrix form
    print("\n給人看的:")
    for i, row in enumerate(grid):
        if i % 3 == 0 and i != 0:
            print("- - - + - - - + - - -")
        for j, num in enumerate(row):
            num_str = str(num) if num != 0 else f"\033[37m.\033[0m"
            print(f"\033[36m{num_str}\033[0m", end=" ")
            if j == 2 or j == 5:
                print("|", end=" ")
        print()
    print()


def main(run_times, output_file, file_path, delay_seconds=1, continue_last=False):
    if not continue_last and os.path.exists(output_file):
        os.remove(output_file)

    last_run_number = get_last_run_number(output_file) if continue_last else 0

    for run_number in range(last_run_number + 1, last_run_number + run_times + 1):
        sudoku_puzzle = load_sudoku(file_path)
        clear()
        if sudoku_puzzle:
            print(f"Run Number: {run_number}")
            print_sudoku_q(sudoku_puzzle, "題目")
            solvable, filled_grid, errors = is_solvable(sudoku_puzzle)
            save_to_file(run_number, solvable, sudoku_puzzle, filled_grid if solvable else ['none'], output_file, 'a')
            if solvable:
                print_sudoku(filled_grid, "解答")
            else:
                print("\n無解的區域:")
                print_sudoku_with_errors(filled_grid, errors)

            time.sleep(delay_seconds)
        else:
            print("The sudoku puzzle format is incorrect.")


# User input
if __name__ == '__main__':
    run_times = int(input("Enter the number of times you want to run the sudoku solver: "))
    continue_last_input = input("Do you want to continue from the last run? (yes/no): ")
    continue_last = continue_last_input.strip().lower() == 'yes'
    output_file = "sudoku_results.txt"
    file_path = 'sudoku.txt'
    delay_seconds = 1

    main(run_times, output_file, file_path, delay_seconds, continue_last)
