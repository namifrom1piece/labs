#####################################################
# APS106 Winter 2024 - Lab 6 - Chemical Eqn Checker #
#####################################################

######################################################
# PART 1 - Molecular Formula to Dictionary Converter #
######################################################

def molecule_formula(compound_formula):
    """
    (str) -> dictionary

    When passed a string of the compound formula, returns a dictionary 
    with the elements as keys and the number of atoms of that element as values.
    
    Parameters
    ----------
    compound_formula : str
        A string representing a chemical compound formula. The formula
        is a combination of element symbols and numbers. The element
        symbols are a single uppercase letter, followed by zero or more
        lowercase letters. The numbers are integers.
    
    Returns
    -------
    dictionary
        A dictionary with the elements as keys and the number of atoms of
        that element as values.

    Examples
    --------
    >>> molecule_formula("C2H6O1")
    {'C': 2, 'H': 6, 'O': 1}

    >>> molecule_formula("C1H4")
    {'C': 1, 'H': 4}
    """
    ## To Do: Complete the function
    
    i = 0
    molecule_dictionary = {}
    
    capital_indices = []
    for i in range(len(compound_formula)):
        if compound_formula[i].isupper():
            capital_indices.append(i)
    
    capital_indices.append(len(compound_formula))

    for i in range(1,len(capital_indices)):
        element_substr = compound_formula[capital_indices[i-1]:capital_indices[i]]
            
        if element_substr[1].isalpha():
            elem_len = 2
        else:
            elem_len = 1
        
        elem = element_substr[:elem_len]
        num = int(element_substr[elem_len:])

        if elem in molecule_dictionary:
            molecule_dictionary[elem] += num
        else:
            molecule_dictionary[elem] = num

    return molecule_dictionary

print(molecule_formula('C2H6O1'))



######################################################
# PART 2 - Chemical Expression to Element Dictionary #
######################################################
    
def expression_formula(expr_coeffs, expr_molecs):
    """
    (tuple (of ints), tuple (of dictionaries)) -> dictionary
    
    Calculate the total number of atoms of each element in a chemical expression.
    
    Parameters
    ----------
    expr_coeffs : tuple
        A tuple containing integers that represent the coefficients for molecules
        within the expression. The order of the coefficients correspond to the order
        of molecule dictionaries.
    expr_molecs : tuple
        A tuple containing dictionaries that define the molecules within the expression.
        The molecule dictionaries have the form {'atomic symbol' : number of atoms}.
        The order of the coefficients correspond to the order of molecule dictionaries.
    
    Returns
    -------
    dictionary
        A dictionary containing all elements within the expression as keys and the
        corresponding number of atoms for each element within the expression as values.

    Examples
    --------
    
    >>> # expression: 2NaCl + H2 + 5NaF
    >>> expression_formula((2,1,5), ({"Na":1, "Cl":1}, {"H":2}, {"Na":1, "F":1}))
    {'Na': 7, 'Cl': 2, 'H': 2, 'F': 5}
    
    """
    ## To Do: Complete the function
    total_atoms = {}

    for i in range(len(expr_coeffs)):
        coefficent = expr_coeffs[i]
        molecule_dict = expr_molecs[i]
        
        for element, count in molecule_dict.items():
            if element in total_atoms: 
                total_atoms[element] += coefficent * count
            else:
                total_atoms[element] = coefficent * count
    
    return total_atoms

print(expression_formula((2,1,5), ({"Na":1, "Cl":1}, {"H":2}, {"Na":1, "F":1})))
    
########################################################
# PART 3 - Identify Unbalanced Atoms in a Chemical Eqn #
########################################################

def identify_unbalanced_atoms(reactant_atoms, product_atoms):
    """
    (Dict,Dict) -> Set
    
    Identify the elements that are not balanced between two dictionaries 
    that represent two sides of a chemical equation.
    
    Parameters
    ----------
    reactant_atoms : Dict
        A dictionary containing the elements and the number of atoms of
        each element on the reactant side of a chemical equation.
    product_atoms : Dict
        A dictionary containing the elements and the number of atoms of
        each element on the product side of a chemical equation.

    Returns
    -------
    Set
        A set containing all the elements that are not balanced between
        the two dictionaries.

    
    Examples
    --------
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 1, "Cl" : 2})
    {'Na'}
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 2, "Cl" : 2})
    set()
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "F" : 2, "Cl" : 2})
    {'F', 'Na'}
    """
    ## To Do: Complete the function
    
    unbalanced_el = set()

    all_elements = set(reactant_atoms.keys()).union(set(product_atoms.keys()))

    for element in all_elements:
        
        if reactant_atoms.get(element, 0) != product_atoms.get(element, 0):
            unbalanced_el.add(element)

    return unbalanced_el

print(identify_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 1, "Cl" : 2})) # should print "{'Na'}"
print(identify_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 2, "Cl" : 2})) # should print "set()"
print(identify_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "F" : 2, "Cl" : 2})) # should print "{'Na', 'F'}"

###############################################
# PART 4 - Check Chemical Equation Balance    #
###############################################

def check_eqn_balance(reactants, products):
    """
    (tuple,tuple) -> Set
    
    Check if a chemical equation is balanced. Return any unbalanced
    elements in a set.
    
    Both inputs are nested tuples. The first element of each tuple is a tuple
    containing the coefficients for molecules in the reactant or product expression.
    The second element is a tuple containing strings of the molecules within
    the reactant or product expression. The order of the coefficients corresponds
    to the order of the molecules. The function returns a set containing any
    elements that are unbalanced in the equation.
    
    Parameters
    ----------
    reactants : tuple
        A two-element nested tuple containing the coefficients for molecules 
        in the reactant expression and the molecules themselves. 
    products : tuple
        A two-element nested tuple containing the coefficients for molecules
        in the product expression and the molecules themselves.

    Returns
    -------
    Set
        A set containing any elements that are unbalanced in the equation.
    
    Examples
    --------
    >>> # balanced equation: C3H8 + 5O2 <-> 4H2O + 3CO2
    >>> check_eqn_balance(((1,5), ("C3H8","O2")),((4,3), ("H2O1","C1O2")))
    set()

    >>> # unbalanced equation: C3H8 + 2O2 <-> 4H2O + 3CO2
    >>> check_eqn_balance(((1,2), ("C3H8","O2")),((4,3), ("H2O1","C1O2")))
    {'O'}
    """
    ## To Do: Complete the function
    
    react_molecules = tuple(molecule_formula(m) for m in reactants[1])
    prod_molecules = tuple(molecule_formula(m) for m in products[1])

    reactant_atoms = expression_formula(reactants[0], react_molecules)
    product_atoms = expression_formula(products[0], prod_molecules)

    
    return identify_unbalanced_atoms(reactant_atoms, product_atoms)

print(check_eqn_balance(((1,2), ("C3H8","O2")),((4,3), ("H2O1","C1O2")))) # should print "{'O'}""
print(check_eqn_balance(((1,5), ("C3H8","O2")),((4,3), ("H2O1","C1O2")))) # should print "set()"
