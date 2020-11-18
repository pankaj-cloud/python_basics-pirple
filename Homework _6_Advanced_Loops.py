"""
Homework Assignment #6: Advanced Loops
Create a function that takes in two parameters: rows, and columns, both of which are integers.
The function should then proceed to draw a playing board (as in the examples from the lectures)
the same number of rows and columns as specified. After drawing the board, your function should return True.
"""

def create_board(rows, columns):
    rows = int(rows)
    columns = int(columns)
    if columns <= 10 and rows <= 10:
        for row in range(rows):
            if row % 2 == 0:
                for col in range(1, columns):
                    if col % 2 == 1:
                        if col != columns - 1:
                            print(" ", end="")
                        else:
                            print(" ")
                    else:
                        print("|", end="")
            else:
                print("-" * columns)
        # After drawing is done return True
        return True
create_board(10, 10)