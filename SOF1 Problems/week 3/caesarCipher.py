"""
Exercise 5 of week 3; this program encrypts and decrypts sentences using the caesar cipher
Author: Ethan Davis
"""

SHIFT = 13
#I am not sure if the preferred solution uses a list of the alphabet or the ASCII value of the letters, but since I don't think I've seen chr() or ord() yet I am inclined to use the list
ALPHA_LIST = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_encrypt_ascii():
    plain_sent = str(input("Enter the sentence you would like to encrypt: "))
    encrypted_sent = ""
    for char in plain_sent:
        offset = 65
        if char.islower():
            offset += 32
        encrypted_sent += chr((ord(char) + SHIFT - offset) % 26 + offset)
    return encrypted_sent

def caesar_encrypt_list():
    plain_sent = str(input("Enter the sentence you would like to encrypt: "))
    encrypted_sent = ""
    for char in plain_sent:
        encrypt_letter = ALPHA_LIST[(ALPHA_LIST.index(char.lower()) + SHIFT) % 26]
        if char.isupper():
            encrypt_letter = encrypt_letter.upper()
        encrypted_sent += encrypt_letter
    return encrypted_sent

def main():
    #print(caesar_encrypt_ascii())
    print(caesar_encrypt_list())

main()