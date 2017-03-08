import numpy as np
from node import Node

def get_row(index, arr):
    return arr[index, :]


def get_col(index, arr):
    return arr[:, index]


def get_grid(index, arr):
    options = {0: arr[0:3, 0:3],
               1: arr[0:3, 3:6],
               2: arr[0:3, 6:9],
               3: arr[3:6, 0:3],
               4: arr[3:6, 3:6],
               5: arr[3:6, 6:9],
               6: arr[6:9, 0:3],
               7: arr[6:9, 3:6],
               8: arr[6:9, 6:9]
               }

    return options[index]


def get_all_rows(arr):
    rows = []
    for row_index in range(len(arr)):
        rows.append(get_row(row_index, arr))
    return rows


def get_all_cols(arr):
    cols = []
    for col_index in range(len(arr)):
        cols.append(get_col(col_index, arr))
    return cols


def get_all_grids(arr):
    grids = []
    for grid_index in range(len(arr)):
        grids.append(get_grid(grid_index, arr))
    return grids


def get_possible_digits(arr):
    all_digits = range(1, 10)
    return [x for x in all_digits if x not in arr]


def get_grid_containing_position(x, y, arr):
    if x <= 2:
        if y <= 2:
            return get_grid(0, arr)
        elif y <= 5:
            return get_grid(1, arr)
        elif y <= 8:
            return get_grid(2, arr)
    elif x <= 5:
        if y <= 2:
            return get_grid(3, arr)
        elif y <= 5:
            return get_grid(4, arr)
        elif y <= 8:
            return get_grid(5, arr)
    elif x <= 8:
        if y <= 2:
            return get_grid(6, arr)
        elif y <= 5:
            return get_grid(7, arr)
        elif y <= 8:
            return get_grid(8, arr)


def get_possible_digits_at_position(x, y, arr):
    """Return a list of possible digits at position (x,y)
    This function enforces the rules of sudoku and returns
    a list of all possible digits at position (x,y). Handy for
    creating a tabu list.
    """
    if int(arr[x, y]) is not 0:
        return None

    row_vals = list(filter(lambda a: a != 0, get_row(x, arr)))
    col_vals = list(filter(lambda a: a != 0, get_col(y, arr)))
    # flatten the grid array into one-dimensional array
    grid_vals = list(filter(lambda a: a != 0, np.hstack(get_grid_containing_position(x, y, arr))))
    uniques = list(set().union(row_vals, col_vals, grid_vals))

    return get_possible_digits(uniques)


def calculate_score(arr):
    """" Calculates the score of the sudoku board.
        The maximum score is 81 when every digit has been filled in
    """
    return np.count_nonzero(arr)


def is_best_solution(arr):
    return calculate_score(arr) == 81


def get_empty_positions(arr):
    """ Returns a list of tuples (x,y) of the positions on the sudoku board which are empty
        and are possible candidates to be filled out by the player/ant
    """
    return np.asarray(np.where(arr == 0)).T


def set_digit_at_position(x, y, digit, arr):
    arr[x][y] = digit
    return arr


def has_empty_positions(arr):
    empty_positions = get_empty_positions(arr)
    if empty_positions is None or len(empty_positions) == 0:
        return False
    return True

