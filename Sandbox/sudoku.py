'''Sudoku solver'''
from playwright.sync_api import Page

def find_next_empty(puzzle):
    ''' finds the next row, col on the puzzle that's not filled yet --> rep with -1''
        return row, col tuple (or (None, None) if there is none)
    '''
    # keep track of row and col
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == -1:
                return row, column
    return None, None # if no spaces in the puzzle are empty (-1)

def is_valid(puzzle, guess, row, col):
    ''' figures out whether the guess at the row/col of the puzzle is a valid guess
        returns True or False
    '''
    # check row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # check column
    col_vals = [puzzle[row_check][col] for row_check in range(9)]
    if guess in col_vals:
        return False

    # check square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for row_check in range(row_start, row_start + 3):
        for column_check in range(col_start, col_start + 3):
            if puzzle[row_check][column_check] == guess:
                return False

    # if we get here, these checks pass
    return True

def solve_sudoku(puzzle):
    '''Sudoku solver'''
    # solve sudoku using backtracking algorithm
    # return solution
    # mutates puzzle to be the solution (if solution exists)

    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)
    if row is None:
        return True

    # step 2: make a guess (1-9)
    for guess in range(1, 10):
        # step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is valid, then place that guess on the puzzle!
            puzzle[row][col] = guess
            # step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True
        # step 5: if not valid OR if our guess does not solve the puzzle, then we need to
        # backtrack and try a new number
        puzzle[row][col] = -1 # reset the guess

    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
    return False

if __name__ == '__main__':
    example_board = [[-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
                     [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
                     [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],

                    [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
                    [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
                    [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],

                    [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
                    [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
                    [-1, -1, -1,  -1, -1, -1,  -1, -1, -1]]


    print(solve_sudoku(example_board))
    print(example_board)


    # example_board = [[-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
    #                  [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
    #                  [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],

    #                 [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
    #                 [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
    #                 [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],

    #                 [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
    #                 [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
    #                 [-1, -1, -1,  -1, -1, -1,  -1, -1, -1]]
