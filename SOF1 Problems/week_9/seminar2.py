"""
Solution for week 9 seminar exercise 2
Author: Ethan Davis
"""

def max_cheese(case_allowance, *cheeses):
    """Finds the maximum value of cheese you can get in a suitcase

    Args:
        case_allowance (_type_): _description_
    """
    chz_sorted = ppg_sorter(cheeses)
    print(chz_sorted)
    
def ppg_sorter(cheese_list):
    """

    Args:
        cheese_list (_type_): _description_
    """
    cheeses = list(cheese_list)
    for i in range(len(cheeses)-1):
        for j in range(i,len(cheeses)-1):
            if cheeses[i][0]/cheeses[i][1] < cheeses[i+1][0]/cheeses[i+1][1]:
                popped = cheeses.pop(i+1)
                cheeses.insert(i, popped)
    return cheeses


def main():
    cheese1, cheese2, cheese3 = (3000,150), (2000,80), (3000,190)
    print(max_cheese(6000, cheese1, cheese2, cheese3))

if __name__ == "__main__":
    main()