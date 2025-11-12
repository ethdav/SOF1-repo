"""
All of the exercises for week 7.
Author: Ethan Davis
"""
from string import punctuation as punctuation
import math

def format_string(string):
    """Quick formatting function

    Args:
        string (_type_): _description_

    Returns:
        _type_: _description_
    """
    string = string.lower()
    formatted = ""
    for index in string:
        if index.isalpha():
            formatted += index
    return formatted

def ispalindrome(word, index=0):
    """Recursively determines if a word is a palindrome

    Args:
        word (str): the word passed in to be determined if a palindrome
    """
    if word.isalpha() is False:
        return ispalindrome(format_string(word))
    length = len(word)
    if index == 1+length//2:
        return True
    elif word[index] == word[length-index-1]:
        index += 1
        return ispalindrome(word, index)
    else:
        return False

def rec_sum(list, index=0, sum=0):
    """Recursively finds the sum of a list

    Args:
        list (_type_): _description_
        index (int, optional): _description_. Defaults to 0.
        sum (int, optional): _description_. Defaults to 0.
    """
    length = len(list)
    if length == 0:
        return sum
    elif index == length:
        return sum
    else:
        new_sum = list[index] + sum
        index += 1
        return rec_sum(list, index, new_sum)

def rec_sum_digits(number, sum=0, i=0):
    """Recursive func for finding the sum of the digits of a number

    Args:
        number (_type_): _description_
        i (int, optional): _description_. Defaults to 0.
    """
    k = math.floor(math.log10(number))
    if i > k:
        return sum
    else:
        new_sum = sum + ((number%(10**(i+1)))-(number%(10**i)))/(10**i)
        i += 1
        return rec_sum_digits(number, new_sum, i)

def flatten(mlist, flattened=[], index=0):
    """Recurisively flattens a multidimensional list, ignoring empty lists

    Args:
        mlist (_type_): _description_
    """
    length = len(mlist)
    if index == length:
        return flattened
    else:
        if isinstance(mlist[index], list):
            flatten(mlist[index], flattened)
        else:
            flattened.append(mlist[index])
        index+=1
        return flatten(mlist, flattened, index)

def main():
    # word_1 = "Live on time, emit no evil"
    # print(ispalindrome(word_1))
    # num_list = [3,4,-1,7,2,-3]
    # empty_list = []
    # print(rec_sum(num_list),"\n",rec_sum(empty_list))
    # number = 1234
    # print(rec_sum_digits(number))
    mlist = [[1,2],[],3,[4,5,6]]
    print(flatten(mlist))

if __name__ == "__main__":
    main()