"""
Week 4's exercise problems
Author: Ethan Davis
"""

def sum_digits(number):
    sum = 0
    for num in str(number):
        sum += int(num)
    return sum

def pairwise_digits(number_a, number_b):
    if len(str(number_a)) > len(str(number_b)):
        longer = str(number_a)
        shorter = str(number_b)
    else:
        longer = str(number_b)
        shorter = str(number_a)
    result = ""
    index = 0
    while index < len(shorter):
        if longer[index] == shorter[index]:
            result += "1"
        else:
            result += "0"
        index+=1
    result += "0"*(len(longer)-len(shorter))
    return result

def to_base10(binary):
    binary = str(binary)
    base10 = 0
    index = 0
    for digit in range(len(binary)-1,-1,-1):
        if binary[digit] == "1":
            base10 += 2**index
        index+=1
    return base10

def main():
    #print(sum_digits(1234))
    #print(pairwise_digits(111,111111))
    print(to_base10(10001011))

main()