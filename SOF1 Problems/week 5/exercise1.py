"""
displays a given dictionary, one key value pair per line
Author: Ethan Davis
"""

def display_dict(dico):
    for key, value in dico.items():
        print(key, "-->", value)

def main():
    dico = {"un":1, "deux":2, "trois":3}
    display_dict(dico)

main()