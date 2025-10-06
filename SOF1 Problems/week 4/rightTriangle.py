"""
Exercise 4 of Week 4; this program returns a right triangle composed of alternating 1's and 0's with a height input by the user
Author: Ethan Davis
"""

def recursive_triangle(rows, curr_row=1):
    """
    Prints a right triangle with alternating 1's and 0's using recursion
    """
    if curr_row > rows:
        return
    else:
        print_row = ""
        for item in range(curr_row):
            print_row += str((curr_row + item)%2)   #this formula is used to alternate between 1's and 0's, even between lines
        print(print_row)
        recursive_triangle(rows, curr_row+1)

def main():
    recursive_triangle(10)

main()