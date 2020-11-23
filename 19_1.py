#!python3

'''Day 19.'''

INPUT = '''Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => OMg
e => NAl'''


molecule = 'ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF'
END_MOLECULE = molecule
END_MOLECULE_LENGTH = len(molecule)
EXCLUDED_STARTS = set(['C', 'P', 'S', 'A', 'T', 'F', 'B', 'M'])
test_molecule = 'HOH'
test2_molecule = 'HOHOHO'

def parse_input(input_string):
    results = []
    for row in input_string.strip().split('\n'):
        m1, m2 = row.split(' => ')
        results.append((m1, m2))
    return results


replacements = parse_input(INPUT)
test_replacements = [('H', 'HO'), ('H', 'OH'), ('O', 'HH')]
test2_replacements = [('e', 'H'), ('e', 'O'), ('H', 'HO'), ('H', 'OH'), ('O', 'HH')]


def generate_molecules_with_replacement(molecule, replacement):
    molecules = set()
    from_atom, to_atom = replacement
    start = 0
    while True:
        position = molecule.find(from_atom, start)
        # print('find', position, molecule, from_atom)
        if position == -1:
            break
        new_molecule = molecule[:position] + to_atom + molecule[position + len(from_atom):]
        molecules.add(new_molecule)
        start = position + 1
    return molecules


def generate_molecules(molecule, replacements):
    molecules = set()
    for replacement in replacements:
        new_molecules = generate_molecules_with_replacement(molecule, replacement)
        molecules.update(new_molecules)
    return molecules


def exclude_molecules(molecules):
    new_molecules = set()
    for m in molecules:
        if len(m) > END_MOLECULE_LENGTH:
            continue
        m_start = m[0]
        if m_start in EXCLUDED_STARTS:
            continue
        new_molecules.add(m)
    return new_molecules


def test():
    print(test_replacements)
    new_molecules = generate_molecules(test_molecule, test_replacements)
    print(new_molecules)


def main1():
    new_molecules = generate_molecules(molecule, replacements)
    print(len(new_molecules))


def main2():
    molecules = set(['e'])
    final_molecule = test_molecule
    step = 0
    while final_molecule not in molecules:
        print(molecules)
        new_molecules = set()
        for m in molecules:
            new_m = generate_molecules(m, replacements)
            new_molecules.update(new_m)
        # print(molecules)
        print(len(molecules))
        molecules = new_molecules
        molecules = exclude_molecules(molecules)
        step += 1
        # print(molecules)
        # input()
    print(step)


if __name__ == '__main__':
    test()
    main1()
    main2()
