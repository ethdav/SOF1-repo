"""
Practice problems for week 2's practical
Author: Ethan Davis
"""

def imperial_to_kg(stones, pounds):
    return (pounds + 14*stones)/2.205 #2.205 is the chosen conversion factor

def kg_to_imperial(kg):
    total = kg * 2.205
    stone = total//14
    pounds = total%14
    return stone, pounds

def user_choice():
    _ = True
    while _ is True:
        conv_choice = input("Type 1 to convert lbs to kgs, or 2 for kgs to lbs\n> ")
        if conv_choice == "1":
            stone = input("Enter stone: ")
            pounds = input("Enter pounds: ")
            kg = imperial_to_kg(int(stone), int(pounds))
            print(stone, "stone and", pounds, "pounds is", kg, "kilograms")
            _ = False
        elif conv_choice == "2":
            kg = input("Enter kilograms: ")
            stone, pounds = kg_to_imperial(int(kg))
            print(kg, "kilograms is", stone, "stone and", pounds, "pounds")
            _ = False
        else:
            print("Invalid value, try again")
            continue

def main():
    user_choice()

main()