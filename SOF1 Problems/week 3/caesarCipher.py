"""
Exercise 5 of week 3; this program encrypts and decrypts sentences using the caesar cipher
Author: Ethan Davis
"""

SHIFT = 13
#I am not sure if the preferred solution uses a list of the alphabet or the ASCII value of the letters, but since I don't think I've seen chr() or ord() yet I am inclined to use the list

def caesar_encrypt():
    plain_sentence = str(input("Enter the sentence you would like to encrypt:"))
