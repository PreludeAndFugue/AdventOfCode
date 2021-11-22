#!python3

from collections import defaultdict
from queue import PriorityQueue
from re import finditer


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

TEST_INPUT = '''e => H
e => O
H => HO
H => OH
O => HH'''

MOLECULE = 'ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF'

TEST_MOLECULE = 'HOH'
TEST_MOLECULE_2 = 'HOHOHO'

START = 'e'

def parse_input(input_string):
    results = defaultdict(list)
    for row in input_string.strip().split('\n'):
        m1, m2 = row.split(' => ')
        results[m1].append(m2)
    return results


REPLACEMENTS = parse_input(INPUT)
# REVERSED_REPLACEMENTS = [(x[1], x[0]) for x in REPLACEMENTS]
TEST_REPLACEMENTS = parse_input(TEST_INPUT)
# REVERSED_TEST_REPLACEMENTS = [(x[1], x[0]) for x in TEST_REPLACEMENTS]

# If a molecule starts with this letter, then it can never be updated to start with 'O'.
EXCLUDED_STARTS = set(['C', 'P', 'S', 'A', 'T', 'F', 'B', 'M'])

GOAL = MOLECULE


def next_molecules(molecule, goal, replacements):
    for k, v in replacements.items():
        for m in finditer(k, molecule):
            start, end = m.span()
            for i in v:
                x = molecule[:start] + i + molecule[end:]
                s = x[0]
                if s in EXCLUDED_STARTS:
                    continue
                if len(x) > len(goal):
                    continue
                # print(m, start, end, x)
                # input()
                yield x


def search(start, goal, replacements):
    # seen_depths = set()
    seen = set()
    check = PriorityQueue()
    check.put((0, start))
    while check:
        depth, molecule = check.get()

        # if depth not in seen_depths:
        #     seen_depths.add(depth)
        # print(depth, molecule)
        # input()

        if molecule == goal:
            return depth

        if molecule not in seen:
            seen.add(molecule)
            for next_molecule in next_molecules(molecule, goal, replacements):
                check.put((depth + 1, next_molecule))


def main():
    d = search(START, GOAL, REPLACEMENTS)
    print(d)


if __name__ == '__main__':
    main()
