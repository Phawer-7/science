mendeleev = {'H': 1.00794, 'He': 4.002602, 'Li': 6.941, 'Be': 9.012182, 'B': 10.811, 'C': 12.0107, 'N': 14.0067,
             'O': 15.9994, 'F': 18.9984032, 'Ne': 20.1797, 'Na': 22.98976928, 'Mg': 24.305, 'Al': 26.9815386,
             'Si': 28.0855, 'P': 30.973762, 'S': 32.065, 'Cl': 35.453, 'Ar': 39.948, 'K': 39.0983, 'Ca': 40.078,
             'Sc': 44.955912, 'Ti': 47.867, 'V': 50.9415, 'Cr': 51.9961, 'Mn': 54.938045,
             'Fe': 55.845, 'Co': 58.933195, 'Ni': 58.6934, 'Cu': 63.546, 'Zn': 65.409, 'Ga': 69.723, 'Ge': 72.64,
             'As': 74.9216, 'Se': 78.96, 'Br': 79.904, 'Kr': 83.798, 'Rb': 85.4678, 'Sr': 87.62, 'Y': 88.90585,
             'Zr': 91.224, 'Nb': 92.90638, 'Mo': 95.94, 'Tc': 98.9063, 'Ru': 101.07, 'Rh': 102.9055, 'Pd': 106.42,
             'Ag': 107.8682, 'Cd': 112.411, 'In': 114.818, 'Sn': 118.71, 'Sb': 121.760, 'Te': 127.6,
             'I': 126.90447, 'Xe': 131.293, 'Cs': 132.9054519, 'Ba': 137.327, 'La': 138.90547, 'Ce': 140.116,
             'Pr': 140.90465, 'Nd': 144.242, 'Pm': 146.9151, 'Sm': 150.36, 'Eu': 151.964, 'Gd': 157.25,
             'Tb': 158.92535, 'Dy': 162.5, 'Ho': 164.93032, 'Er': 167.259, 'Tm': 168.93421, 'Yb': 173.04,
             'Lu': 174.967, 'Hf': 178.49, 'Ta': 180.9479, 'W': 183.84, 'Re': 186.207, 'Os': 190.23, 'Ir': 192.217,
             'Pt': 195.084, 'Au': 196.966569, 'Hg': 200.59, 'Tl': 204.3833, 'Pb': 207.2, 'Bi': 208.9804,
             'Po': 208.9824, 'At': 209.9871, 'Rn': 222.0176, 'Fr': 223.0197, 'Ra': 226.0254, 'Ac': 227.0278,
             'Th': 232.03806, 'Pa': 231.03588, 'U': 238.02891, 'Np': 237.0482, 'Pu': 244.0642, 'Am': 243.0614,
             'Cm': 247.0703, 'Bk': 247.0703, 'Cf': 251.0796, 'Es': 252.0829, 'Fm': 257.0951, 'Md': 258.0951,
             'No': 259.1009, 'Lr': 262, 'Rf': 267, 'Db': 268, 'Sg': 271, 'Bh': 270, 'Hs': 269, 'Mt': 278,
             'Ds': 281, 'Rg': 281, 'Cn': 285, 'Nh': 284, 'Fl': 289, 'Mc': 289, 'Lv': 292, 'Ts': 294, 'Og': 294,
             '': 0}


def returnListSubstance(formula: str):
    """
    :param formula: Формула как string. Пример: CH4
    :return: Массив. При использовании CH4 вернет ['C', 'H', 'H', 'H', 'H']
    """
    res = []
    for i in range(len(list(formula))):
        if formula[i].isupper():
            try:
                if formula[i + 1].islower():
                    try:
                        for j in range(int(formula[i + 1])):
                            res.append((formula[i] + formula[i + 1]))
                    except ValueError:
                        res.append((formula[i] + formula[i + 1]))
                else:
                    try:
                        for j in range(int(formula[i + 1])):
                            res.append((formula[i]))
                    except ValueError:
                        res.append((formula[i]))
            except IndexError:
                res.append((formula[i]))

    return res


def returnMr(ElementsList: list) -> int:
    """
    :param ElementsList: Список str элементов как list. Пример: ['C', 'H', 'H', 'H', 'H']
    :return: Молекулярную массу вещества. При передаче ['C', 'H', 'H', 'H', 'H'] вернет 12.0107+1.00794*4 = 16.04246
    """
    try:
        last_list = [mendeleev[Element] for Element in ElementsList]
    except KeyError as ke:
        return f"Element {ke} doesn't exist"

    return sum(last_list)