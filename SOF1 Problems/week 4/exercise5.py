"""
Debugging and refactoring the code given in exercise 5
Author: Ethan Davis
"""

def sum_lists(list_2D):
    """
    Takes a 2d list and returns a list of the sums of each sub list
    """
    output =[]
    for row in list_2D:
        total = 0
        for val in row:
            total += val
        output.append(total)
    return output

def main():
    data = [[1,2,3], [2], [1, 2, 3, 4]]
    print(sum_lists(data))

main()