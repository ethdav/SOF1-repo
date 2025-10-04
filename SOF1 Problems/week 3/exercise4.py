"""
Exercise 4 of week 3's practice problems; this program will return an input short sentence, and then return the string without whitespaces, w/ out whitespaces in camel case, or a camel case string as a sentence w/ whitespaces
Author: Ethan Davis
"""

def only_whitespace():  #exercise 4a
    sentence = str(input("Enter a sentence: "))
    no_spaces = ""
    for char in sentence:
        if char != " ":
            no_spaces += char
    return no_spaces

def sent_to_camel_case():   #exercise 4b
    sentence = str(input("Enter a sentence: "))
    camel_case = sentence[0].upper()    #the first letter is always upper (not real camel case but whatever)
    index = 1   #we can skip the first index due to line above
    while index < len(sentence):
        if sentence[index] == " ":
            index+=1
            camel_case += sentence[index].upper()
        else:
            camel_case += sentence[index].lower()
        index+=1
    return camel_case

def camel_case_to_list():
    camel_case = str(input("Enter a sentence in camel case: "))
    word_list = []
    temp_word = ""
    for char in camel_case:     #I don't like this, and it could possibly be done better with a while loop
        if char == char.upper():
            if len(temp_word) > 0:
                word_list.append(temp_word)
            temp_word = char
        else:
            temp_word += char
    word_list.append(temp_word)
    return word_list


def main():
    #print(only_whitespace())
    #print(sent_to_camel_case())
    print(camel_case_to_list())

main()