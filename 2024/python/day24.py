
from operator import and_, or_, xor

from help import get_input

test1 = '''x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02'''

test2 = '''x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj'''


def parse(source):
    a, b = source.split('\n\n')
    inputs = {}
    for line in a.split('\n'):
        x, y = line.split(': ')
        inputs[x] = int(y)
    gates = {}
    for line in b.split('\n'):
        x, y = line.split(' -> ')
        x1, x2, x3 = x.split(' ')
        match x2:
            case 'AND':
                x2 = and_
            case 'OR':
                x2 = or_
            case 'XOR':
                x2 = xor
            case _:
                raise ValueError
        gates[y] = x1, x2, x3
    return inputs, gates


# source = test1.strip()
# source = test2.strip()
source = get_input(24)
inputs, gates = parse(source)

# print(inputs, gates)

while gates:
    for k, (in1, op, in2) in gates.items():
        if in1 in inputs and in2 in inputs:
            n1 = inputs[in1]
            n2 = inputs[in2]
            inputs[k] = op(n1, n2)
            del gates[k]
            break

x = sorted(((k, v) for k, v in inputs.items() if k.startswith('z')), reverse=True)
x = ''.join(str(a[1]) for a in x)
print(int(x, base=2))
