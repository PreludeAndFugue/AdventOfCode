#!python3


from search import iddfs
from search import dfs


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
    results = []
    for row in input_string.strip().split('\n'):
        m1, m2 = row.split(' => ')
        results.append((m1, m2))
    return results


REPLACEMENTS = parse_input(INPUT)
REVERSED_REPLACEMENTS = [(x[1], x[0]) for x in REPLACEMENTS]
TEST_REPLACEMENTS = parse_input(TEST_INPUT)
REVERSED_TEST_REPLACEMENTS = [(x[1], x[0]) for x in TEST_REPLACEMENTS]

GOAL = MOLECULE


def children(node):
    for k, v in REVERSED_REPLACEMENTS:
        if k in node:
            yield node.replace(k, v, 1)


def main():
    r = iddfs.id_dfs(MOLECULE, children, START)
    # r = dfs.dfs_iterative(MOLECULE, children, START)
    print(r)


if __name__ == '__main__':
    main()
