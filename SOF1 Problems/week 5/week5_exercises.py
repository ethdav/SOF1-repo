"""
Collection of exercises from week 5
Author: Ethan Davis
"""

def concat_dico(dico1, dico2):
    """Concatenates two dicts without altering them.
    Args: 
        dico1 = a dictionary of arbitrary length
        dico2 = another dict of arbitrary length
    Returns:
        A dictionary that is dico1 + dico2. If dico1 and dico2 share
        any keys, then the values will be added to a list represented
        by that key in the returned dict.
    """
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

def map_list(keys,values):
    if len(keys) != len(values):
        print("Lists not same length")
        return
    dict_map = dict()
    for index in range(len(values)):
        if keys[index] in dict_map.keys():
            print("Duplicate keys")
            return
        dict_map[keys[index]] = values[index]
    return dict_map

def reverse_dict(dico):
    new_dico = dict()
    for key in dico.keys():
        if dico[key] in new_dico.keys():
            print("duplicate values resulting in duplicate keys")
            return
        new_dico[dico[key]] = key
    return new_dico

def main():
    # dico1 = {1:"a",2:"b",3:"c"}
    # dico2 = {3:"d",4:"e",2:10}
    # display_dict(concat_dico(dico1,dico2))
    keys = [1,2,3,]
    values = ["un","deux","trois"]
    dico = map_list(keys,values)
    print(dico)
    print(reverse_dict(dico))

main()