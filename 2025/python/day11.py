from copy import deepcopy
from queue import Queue

test = '''aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out'''

test2 = '''svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out'''


source = test.strip()
source = test2.strip()
source = open('day11.txt', 'r').read().strip()

map_ = {}
for line in source.split('\n'):
    l1, l2 = line.split(': ')
    l2 = l2.split(' ')
    map_[l1] = l2
# print(map_)


def delete_node(v, map_):
    new_map_ = {}
    for k, values in map_.items():
        if k == v:
            continue
        new_values = deepcopy(values)
        if v in values:
            new_values.remove(v)
        new_map_[k] = new_values
    return new_map_


def dead_ends(map_):
    x = []
    for k, v in map_.items():
        if k == 'out':
            continue
        if not v:
            x.append(k)
    print(x)


def false_starts(map_):
    all_values = set()
    all_keys = set()
    for k, values in map_.items():
        all_keys.add(k)
        all_values.update(values)
    x = all_keys - all_values
    x -= set(['svr'])
    print(x)


to_delete = [
    # to fft
    'epi','iwn','alg','xbo','ckd','nnz','pza','qma','xxc','vby','fln','mrt','aiu','szx',
    'tcc','vlu','wqn','gch','knr','qhy','bgp','miy','klz','wyp','jze',

    # dead ends
    'jix','kud','nae','gkd','yop','opb','fwu','dvb','qza','src','syu','uxi','qgy','mce',
    'jii','pvm','qgi','ktu','ntj','yls','oxi','ihm','sce',


    'mle','fju','dcu','uqa','lje','dhz','tsv','npm','fuj','ing','wgk','vnr','iiv','vjx',
    'yby','hnc','ecb',

    'szm', 'cab',

    'vqb',

    # false starts
    'lfn', 'aym', 'rzk', 'skf', 'qcf', 'wpv', 'fjn', 'esh', 'pkd', 'kan', 'dja', 'hxq',
    'hby', 'gvn', 'rvp', 'dro', 'kjq', 'luy',

    'iws', 'glt', 'iin', 'tkd', 'gwz', 'kmo', 'kwo', 'jun', 'zlh',

    # to dac
    'gow', 'dio', 'txt', 'pmp', 'net', 'bzn', 'cvl', 'iwr', 'mlg', 'cue', 'vew',
    'hts', 'paf', 'jte', 'dha', 'ica', 'juw', 'qee', 'ypd', 'jvk',
    'wvl', 'utw', 'kcx', 'ane', 'sst', 'pko', 'xac', 'usi',
    'zfo', 'pst', 'zaz', 'eng', 'oeh',
    'rul', 'qap', 'dhr', 'qgv',

    # dead ends
    'jlj', 'lob', 'cyk', 'nqz', 'raa', 'guy',

    # false starts
    'dbp', 'hiy', 'cfh', 'tfz', 'bdq', 'ksz', 'utf', 'che', 'szr', 'jfb', 'btl', 'sbs',
    'vhc', 'tpg', 'eyk', 'flr',
    'zqk', 'qpx', 'wua', 'sqy', 'xah', 'nne', 'hho', 'dho', 'rxz', 'ozs', 'nii', 'amu',
]

for d in to_delete:
    map_ = delete_node(d, map_)

dead_ends(map_)
false_starts(map_)


with open('graph11.txt', 'w') as f:
    for k, v in map_.items():
        for w in v:
            f.write(f'{k} -> {w}\n')



def part1():
    # start = 'you'
    # end = 'out'
    start = 'fft'
    end = 'dac'
    q = Queue()
    q.put(start)
    count = 0
    while not q.empty():
        v = q.get()
        if v == end:
            count += 1
            continue
        for w in map_[v]:
            q.put(w)

    print(count)


# Paths from svr to fft: 2588

# Paths from fft to dac: 18007824

# Paths from dac to out: 10289


# part1()

print(2588*18007824*10289)