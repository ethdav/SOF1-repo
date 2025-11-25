"""
Solution for week 9 seminar exercise 2
Author: Ethan Davis
"""

def max_cheese(case_allowance, *cheeses):
    """Finds the maximum value of cheese you can get in a suitcase

    Args:
        case_allowance (_type_): _description_
    """
    chz_list = [x for x in cheeses]
    for i in range(1,len(chz_list)):
        if chz_list[i-1][1]/chz_list[i][0] > chz_list[i][1]/chz_list[i][0]:
            popped = chz_list.pop(i)
            chz_list.insert(i-1,popped)
    

def main():
    cheese1, cheese2, cheese3 = (3000,150), (2000,80), (3000,190)
    print(max_cheese(6000, cheese1, cheese2, cheese3))

if __name__ == "__main__":
    main()