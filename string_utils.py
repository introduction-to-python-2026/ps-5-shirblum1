def split_before_uppercases(formula):
    if not formula:
        return []

    elements = []
    current = formula[0]

    for ch in formula[1:]:
        if ch.isupper():
            elements.append(current)
            current = ch
        else:
            current += ch

    elements.append(current)
    return elements


def split_at_digit(formula):
    for i, ch in enumerate(formula):
        if ch.isdigit():
            return formula[:i], int(formula[i:])
    return formula, 1


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
    reaction_equation = reaction_equation.replace(" ", "")
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")


def count_atoms_in_reaction(molecules_list):
    return [count_atoms_in_molecule(molecule) for molecule in molecules_list]
