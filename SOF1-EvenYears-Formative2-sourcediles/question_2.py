"""
Answer to question 2 for Formative 2
"""

def common_values(lst1, lst2):
    """Returns a list of all of the shared values between two lists

    Args:
        lst1 (list): list 1 to be compared
        lst2 (list): list 2 to be compared
    
    Returns:
        A list containing the common values.
    """
    set1 = set(lst1)
    common = set()
    for value in lst2:
        if value in set1:
            common.add(value)
    return list(common)

def main():
    lst1 = [2,4,6,8]
    lst2 = [1,3,5,7,9]
    print(common_values(lst1, lst2))

if __name__ == "__main__":
    main()