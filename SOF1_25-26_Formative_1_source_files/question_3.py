ATOMS = {"H":{"name":"Hydrogen", "weight":1.00797},
         "He":{"name":"Helium", "weight":4.00260},
         "C":{"name":"Carbon", "weight":12.011},
         "O":{"name":"Oxygen", "weight":15.9994}}

def molar_mass(molecule):
    """Takes a list of tuples representing a molecule and returns its molar mass.

    Args:
        molecule (list): a list of tuples to represent a molecule; ie. H2O -> [('H',2),('O',1)]

    Returns:
        The molar mass of a molecule.
    """
    molar_mass = 0
    for atom in molecule:
        if atom[0] not in ATOMS:
            return None
        molar_mass += ATOMS[atom[0]]["weight"] * atom[1]
    return molar_mass