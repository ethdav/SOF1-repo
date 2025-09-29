"""
practice with for loops
"""

def exercise_a():
    integer_n = int(input("Enter a positive integer: "))
    sum = 0
    for x in range(0, integer_n+1): #add 1 to include given integer in loop
        if x%2 == 0:
            sum += x
    print("The sum of all even integers less than or equal to", integer_n, "is", sum)

def exercise_b():
    #I am unsure what this problem wants from me
    pass

def exercise_c():
    #prints the factorial of the given integer
    int_n = int(input("Enter a positive integer: "))
    factorial = 1
    for x in range(int_n):
        factorial = factorial * (x+1) #1 is added to start the range at 1 and end at the given int
    print(int_n, "factorial is", factorial)

def main():
    #exercise_a()
    exercise_c()

main()