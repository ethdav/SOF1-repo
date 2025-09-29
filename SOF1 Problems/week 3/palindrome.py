"""
This program determines if a given string is a palindrome
Author: Ethan Davis
"""

def format_string():
    string = str(input("Enter a string: "))
    string_list = []
    for char in string:
        if char.isalpha():
            string_list.append(char)
    print(string_list)

def is_palindrome(string_list):
    for letter in len(string_list)//2: #floor division to get half of the list regardless if odd or even
        if string_list[letter] == string_list[len(string_list)-letter]:
            continue
        else:
            print("The given word is not a palindrome")
            break

def main():
    string_list = format_string()
    is_palindrome(string_list)

main()