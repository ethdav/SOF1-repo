def molecule_to_list(molecule):
    """Takes a string representing a molecule and returns a list of
    tuples, each tuple containing the atom and its number.

    Args:
        molecule (str): a string representing a molecule, such as "H2O"

    Returns:
        A list of tuples containing the information of a molecule. For
    example, "H2O" would return [('H',2),('O',1)].
    """
    if molecule[0].isupper() is False or molecule.isalnum() is False:
        return None
    mol_list = []
    for index in range(len(molecule)):
        if molecule[index].isupper():
            mol_list.append([molecule[index],1])
        elif molecule[index].isalpha():
            if molecule[index-1].isupper():
                mol_list[-1][0] += molecule[index]
            else:
                return None
        elif molecule[index].isnumeric():
            if molecule[index-1].isnumeric():
                mol_list[-1][1] = int(molecule[index-1]+molecule[index])
            else:
                mol_list[-1][1] = int(molecule[index])
    for item in range(len(mol_list)):
        mol_list[item] = tuple(mol_list[item])
    return mol_list
