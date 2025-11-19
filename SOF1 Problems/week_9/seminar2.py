"""
Solution for week 9 seminar exercise 2
Author: Ethan Davis
"""

def max_cheese(case_allowance, *cheeses):
    """Finds the maximum value of cheese you can get in a suitcase

    Args:
        case_allowance (_type_): _description_
    """
    pricePerGram = []
    for cheese in cheeses:
