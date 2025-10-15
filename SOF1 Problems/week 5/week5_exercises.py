"""
Collection of exercises from week 5
Author: Ethan Davis
"""

def concat_dico(dico1, dico2):
    concatted = dico1
    for key in dico2.keys():
        if key not in concatted.keys():
            concatted[key] = dico2[key]
        else:
            concatted[key] = [concatted[key], dico2[key]]
    return concatted

def display_dict(dico):
    for key, value in dico.items():
        print(key, "-->", value)

def main():
    dico1 = {1:"a",2:"b",3:"c"}
    dico2 = {3:"d",4:"e",2:10}
    display_dict(concat_dico(dico1,dico2))

main()