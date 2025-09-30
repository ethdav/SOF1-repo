"""
Takes the sides of a triangle from the user and prints the area using Heron's formula
It does not have input validation
Author: Ethan Davis
"""

def find_area():
    a = int(input("Enter side a: "))    #I hate using single letter variables :(
    b = int(input("Enter side b: "))
    c = int(input("Enter side c: "))
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** .5
    print("The area of the given triangle is:", area)

def main():
    find_area()

main()