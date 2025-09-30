"""
Takes the users heart rate and age and determines their "Training Zone"
Author: Ethan Davis
"""

def get_training_zone():
    age = int(input("Enter your age: "))
    rate = int(input("Enter your training heart rate: "))
    max_rate = 208 - 0.7*age
    if rate >= .9*max_rate:
        zone = "Interval Training"
    elif .9*max_rate > rate >= .7*max_rate:
        zone = "Threshold Training"
    elif .7*max_rate > rate >= .5*max_rate:
        zone = "Aerobic Training"
    elif rate > .5*max_rate:
        zone = "Couch Potato"
    else:
        pass
    print("Based on your age and heart rate, your training zone is:\n", zone)

def main():
    get_training_zone()

main()