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

def main():
    #sentences = ["This","is","a","sentence"]
    #filename = "./week_6/exo2.txt"
    #save_list_to_file(sentences,filename)
    entry = "newest entry number 3"
    logfile = "./week_6/log.txt"
    save_to_log(entry, logfile)

main()