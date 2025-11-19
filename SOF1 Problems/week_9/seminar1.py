"""
My solutions to week 9's seminar problems. Fuck pseudocode
Author: Ethan Davis
"""

# We are gonna do maths with whole numbers and then divide the result by 100
DENOMINATIONS = [200, 100, 50, 20, 10, 5, 2, 1]

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
        coin_list = {("£"+str(x/100)):0 for x in DENOMINATIONS}
        for denom in DENOMINATIONS:
            coin_list["£"+str(denom/100)] = shifted // denom
            shifted = shifted % denom
        return coin_list
    
def main():
    total = 143.94
    print(min_coins(total))

if __name__ == "__main__":
    main()