"""
Seminar exercises for week 8
Author: Ethan Davis
"""

def sum_all(num_list, i=0, sum=0):
    """Recursive function for summing all elements in a list, even if
    it is multidimensional

    Args:
        num_list (list): the (multidimensional) list to be summed
        i (int, optional): The index of the current list being looked at
        sum (int, optional): The sum. Defaults to 0.
    """
    if i == len(num_list):
        return sum
    else:
        if isinstance(num_list[i], list):
            sum += sum_all(num_list[i])
        else:
            sum += num_list[i]
        i+=1
        return sum_all(num_list, i, sum)
    
def wildcard(pattern, i=0, solution_set=set()):
    """Given a string of 1's and 0's with wildcard characters (?) mixed
    in, find every possible combination of strings with those wildcards
    being either a 1 or 0

    Args:
        pattern (str): The binary string with wildcards mixed in
        i (int, optional): Index of the string. Defaults to 0.
    """
    if i == len(pattern):
        solution_set.add(pattern)
        return
    else:
        if pattern[i] == "?":
            pattern0 = pattern[0:i] + "0" + pattern[i+1:]
            pattern1 = pattern[0:i] + "1" + pattern[i+1:]
            wildcard(pattern0, i, solution_set)
            wildcard(pattern1, i, solution_set)
            return solution_set
        i+=1
        return wildcard(pattern, i, solution_set)
    
def main():
    pattern = "1?11?00?1?"
    print(wildcard(pattern))

if __name__ == "__main__":
    main()