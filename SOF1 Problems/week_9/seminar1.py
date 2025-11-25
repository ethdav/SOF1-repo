"""
My solutions to week 9's seminar problems. Fuck pseudocode
Author: Ethan Davis
"""

# We are gonna do maths with whole numbers and then divide the result by 100
DENOMS = [200, 100, 50, 20, 10, 5, 2, 1]

def min_coins(total):
    """Finds the minimum number of coins required to sum to the given
    total

    Args:
        total (int, float): The total amount given to find the minimum number
        of coins
    """
    if isinstance(total, (int, float)) is False:
        raise TypeError(f"Invalid type for total:{type(total)}")
    else:
        shifted = total * 100
        coin_list = {("£"+str(x/100)):0 for x in DENOMS}
        for denom in DENOMS:
            coin_list["£"+str(denom/100)] = int(shifted // denom)
            shifted = shifted % denom
        return coin_list
    
def min_coins_recursive(total, id=0, coin_dict={("£"+str(x/100)):0 for x in DENOMS}):
    """Finds the minimum number of coins required to sum to the given
    total recursively

    Args:
        total (_type_): _description_
    """
    if total == 0 or id == len(DENOMS):
        return coin_dict
    else:
        coin_dict["£"+str(DENOMS[id]/100)] = int(total // (DENOMS[id]/100))
        total = total % (DENOMS[id]/100)
        id+=1
        return min_coins_recursive(total, id, coin_dict)

def main():
    total = 19.51
    print(min_coins_recursive(total))

if __name__ == "__main__":
    main()