"""
Lab exercises for week 6
Author: Ethan Davis
"""

def save_str_to_file(a_word, filename):
    """A simple function to write a string to a file

    Args:
        a_word (str): any string
        filename (str): the name of the file being written to
    """
    file = open(filename,"w")
    file.write(a_word)
    file.close()

def save_list_to_file(sentences, filename):
    """Writes each string in a list to a file, one line per element.

    Args:
        sentences (_type_): _description_
        filename (_type_): _description_
    """
    file = open(filename,"w")
    for item in sentences:
        file.write(item + "\n")
    file.close()

def save_to_log(entry, logfile):
    """Appends the entry to the end of the log

    Args:
        entry (_type_): _description_
        logfile (_type_): _description_
    """
    log = open(logfile,"a")
    log.write("\n" + entry)
    log.close()

def read_uppercase(filename):
    """prints the contents of a file in uppercase

    Args:
        filename (_type_): _description_
    """
    file = open(filename,"r")
    print(file.read().upper())
    file.close()

def to_uppper_case(input_file, output_file):
    """reads the contents of one file and outputs it to another file
    in uppercase

    Args:
        input_file (_type_): _description_
        output_file (_type_): _description_
    """
    input_file = open(input_file,"r")
    output_file = open(output_file,"w")
    output_file.write(input_file.read().upper())
    input_file.close()
    output_file.close()

def main():
    filename = "./week_6/exo1.txt"
    read_uppercase(filename)
    output_file = "./week_6/out.txt"
    to_uppper_case(filename, output_file)

main()