"""
Solution for week 9 seminar exercise 2
Author: Ethan Davis
"""

def max_cheese(case_allowance, *cheeses):
    """Finds the maximum value of cheese you can get in a suitcase

    Args:
        case_allowance (_type_): _description_
    """
    pricePerGram = sorted([(x[1]/x[0]) for x in cheeses],reverse=True)
    for cheese in cheeses:
        remainder = None

def main():
    cheese1, cheese2, cheese3 = (3000,150), (2000,80), (3000,190)
    print(max_cheese(6000, cheese1, cheese2, cheese3))

if __name__ == "__main__":
    main()