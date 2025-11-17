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
    
def main():
    multi_list = [1,3,[5,7],9,[1,[2,[3,4]]]]
    print(sum_all(multi_list))

if __name__ == "__main__":
    main()