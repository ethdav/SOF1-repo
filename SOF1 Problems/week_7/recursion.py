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

def merge(alist, blist, merged=[],ia=0, ib=0):
    """Recursively merges two sorted lists in sorted order

    Args:
        alist (list): the first of two sorted lists that are to be merged
        blist (list): the other sorted list to be merged
        merged (list): the resulting merged list
        ia (int): a pointer for the index of list a
        ib (int): a pointer for the index of list b
    """
    if ia == len(alist)-1 and ib == len(blist)-1:
        return merged
    else:
        if ia != len(alist)-1 and ib != len(blist)-1:
            if alist[ia] >= blist[ib]:
                merged.append(blist[ib]); merged.append(alist[ia])
            else:
                merged.append(alist[ia]); merged.append(blist[ib])
            ia+=1
            ib+=1
        elif ia == len(alist)-1:
            merged.append(blist[ib])
            ib+=1
        else:
            merged.append(alist[ia])
            ia+=1
        return merge(alist, blist, merged, ia, ib)

def iselfish(word, i=0 ,char_set=set()):
    """Recursive function for determining if a word is "elfish", ie.
    containing all the letters of the word "elf"

    Args:
        word (str): the word passed in to be determined
        char_set (set, optional): the set of characters from the given
        word that match the letters of "elf". Defaults to {}.
    """
    elf_set = {"e", "l", "f"}
    if char_set == elf_set:
        return True
    elif i == len(word):
        return False
    else:
        if word[i] in elf_set:
            char_set.add(word[i])
        i+=1
        return iselfish(word, i, char_set)

def something_ish(word, pattern, i=0, char_set=set()):
    """Recursive function to see if a given word contains all of the
    letters of the given pattern, in any order.

    Args:
        word (_type_): _description_
        pattern (_type_): _description_
        i (int, optional): _description_. Defaults to 0.
        char_set (_type_, optional): _description_. Defaults to set().
    """
    pattern_set = set(pattern)
    if char_set == pattern_set:
        return True
    elif i == len(word):
        return False
    else:
        if word[i] in pattern_set:
            char_set.add(word[i])
        i+=1
        return something_ish(word, pattern, i, char_set)

def is_power(a,b):
    """Recursive function to determine if a is a power of b

    Args:
        a (_type_): _description_
        b (_type_): _description_
    """
    if a == b:
        return True
    else:
        if a%b == 0 and (a/b)%b == 0:
            return is_power(a/b, b)
        else:
            return False

def main():
    a = 81
    b = 3
    print(is_power(a,b))

if __name__ == "__main__":
    main()