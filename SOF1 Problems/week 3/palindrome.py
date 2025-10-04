"""
This program determines if a given string is a palindrome
Author: Ethan Davis
"""

def format_string():
    string = str(input("Enter a string: "))
    string = string.lower()
    string_list = []
    for char in string:
        if char.isalpha():
            string_list.append(char)
    print(string_list)
    return string_list

def is_palindrome(string_list):
    for letter in range(len(string_list)//2): #floor division to get half of the list regardless if odd or even
        if string_list[letter] == string_list[len(string_list)-1-letter]:
            continue
        else:
            print("The given string is not a palindrome")
            return
    print("The given string is a palindrome")

def main():
    string_list = format_string()
    is_palindrome(string_list)

main()