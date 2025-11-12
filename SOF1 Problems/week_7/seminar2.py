SAMPLE_LIST = [-2,1,-3,4,-1,2,1,-5,4]

def brute_find_sum(list):
    """Brute force version of the required algorithm. Finds the largest
    sum of a sublist within a list.

    Args:
        list (_type_): _description_
    """
    largest = 0
    for index in range(len(list)-1):
        for next_index in range(len(list)):
            if sum(list[index:next_index+1]) > largest:
                largest = sum(list[index:next_index+1])
    return largest

def better_find_sum(list):
    """A slightly smarter (I hope) method of finding the largest sum in
    a list, by first finding all of the indices of the positive values
    and then only checking sublists that begin and end at each stored
    index.

    Args:
        list (_type_): _description_
    """
    pos_indices = []
    

def main():
    print(brute_find_sum(SAMPLE_LIST))

if __name__ == "__main__":
    main()