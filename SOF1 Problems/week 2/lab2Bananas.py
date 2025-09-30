"""
Week 2 exercise 3
"""

def order_cost(kilos):
    cost = (kilos * 3) + 4.99
    if cost >= 50:
        cost -= 1.5
    return cost
    
def user_input():
    kilos = int(input("Enter the number of kilos of bananas to order: "))
    print("Your order of ", kilos, " kgs would cost ", order_cost(kilos))

def main():
    user_input()

main()