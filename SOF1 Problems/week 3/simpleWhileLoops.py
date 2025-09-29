"""
practice with while loops
Author: Ethan Davis
"""

def exercise_a():
    sum = 0
    while True:
        num = int(input("Enter a number: "))
        sum += num
        if num < 0:
            break
        else:
            continue
    print("The sum is:", sum)

def exercise_b():
    sum = 0
    nums_entered = 0
    while True:
        num = int(input("Enter a number: "))
        sum += num
        nums_entered += 1
        if num < 0:
            break
        else:
            continue
    print("The average is", sum/nums_entered)

def exercise_c():
    nums_entered = 0
    while True:
        num = int(input("Enter a number: "))
        if num < 0:
            break
        else:
            nums_entered += 1
            continue
    print("The number of even numbers entered is", nums_entered)

def main():
    #exercise_a()
    #exercise_b()
    exercise_c()

main()