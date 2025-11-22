def split_before_uppercases(formula):
    if formula == "":
        return []

    parts = []
    start = 0

    for i in range(1, len(formula)):
        if formula[i].isupper() nd not formula[i-1].islower():
            parts.append(formula[start:i])
            start = i

    parts.append(formula[start:])
    return parts


def split_at_digit(formula):
    digit_location = 1

    for char in formula[1:]:
        if char.isdigit():
            break
        digit_location += 1

    if digit_location == len(formula):
        return (formula, 1)

    prefix = formula[:digit_location]
    number = int(formula[digit_location:])

    return (prefix, number)



def count_atoms_in_molecule(molecular_formula):
    atoms_count_dict = {}
    for atom_group in split_before_uppercases(molecular_formula):
        atom_name, atom_number = split_at_digit(atom_group)
        if atom_name in atoms_count_dict:
           atoms_count_dict[atom_name] += atom_number
        else:
            atoms_count_dict[atom_name] = atom_number
    return atoms_count_dict



def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace("","")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
