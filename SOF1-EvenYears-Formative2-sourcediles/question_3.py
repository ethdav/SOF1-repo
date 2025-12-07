"""
Answer to question 3 of Formative 2
"""

def read_from_file(filename):
    """Reads a file for the values of an athletes times

    Args:
        filename (_type_): _description_
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