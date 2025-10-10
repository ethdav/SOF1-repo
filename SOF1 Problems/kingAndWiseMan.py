"""
From the additional exercises for week 4, calculating the King and Wise man chess and rice story. For each square of the chess board, the wise man receives an additional doubled number of rice grains
Author: Ethan Davis
"""

BOARD_SIZE = 64

def rice_calculation_for():
    """
    calculates the number of grains using a for loop
    """
    sum = 1     #starts at one to simplify loop
    prev = 1
    for square in range(1,BOARD_SIZE):
        prev = prev * 2
        sum += prev
    return sum

def rice_calc_recursion(sum=0, square=1, prev=0):
    """
    calculates the number of grains using recursion
    """
    if square == BOARD_SIZE:
        sum += prev*2
        return sum
    elif prev == 0:
        return rice_calc_recursion(sum=1,square=square+1, prev=1)
    else:
        curr = prev*2
        sum += curr
        return rice_calc_recursion(sum=sum, square=square+1, prev=curr)

def weight_calc(sum):
    """
    calculates the weight of the sum of the grains of rice
    """
    return sum * .03

def main():
    sum1 = rice_calculation_for()
    sum2 = rice_calc_recursion()
    print(weight_calc(sum1),"kg")
    print(weight_calc(sum2),"kg")


main()