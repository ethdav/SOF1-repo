"""
Answer to question 3 of Formative 2
"""

def read_from_file(filename):
    """Reads a file for the values of an athletes times. It adds their times to a dictionary with the keys as the different events, and then adds those dictionaries to another dict using their names as the keys.

    Args:
        filename (str): the str name of the file to be handled

    Returns:
        A dictionary containing the dictionaries of the athletes times.
    """
    file = open(filename)
    athlete_dict = dict()
    try:
        for line in file:
            if line[0] == "#":
                pass
            else:
                split = line.strip().split(",")
                if len(split) > 4:
                    raise ValueError("File is invalid format")
                times_dict = {"200m":float(split[1]),"110m":float(split[2]),"800m":float(split[3])}
                athlete_dict[split[0]] = times_dict
        return athlete_dict
    except: 
        raise ValueError("File is invalid format")

def main():
    filename = "./data/dataWithoutComments.txt"
    print(read_from_file(filename))

if __name__ == "__main__":
    main()