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

def main():
    sentences = ["This","is","a","sentence"]
    filename = "./week_6/exo2.txt"
    save_list_to_file(sentences,filename)

main()