
from collections import Counter
from copy import deepcopy
from itertools import combinations
import operator

from help import get_input

'''
Part 2
67_782_870_229_872: too low
130_326_142_216_582: too high
'''


TEST = '''px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}'''


def template_function(key, op, test, result):
    def fn(part):
        value = part[key]
        if op(value, test):
            return result
        else:
            return None
    op_str = '<' if op == operator.__lt__ else '>'
    fn.__doc__ = f'{key} {op_str} {test} -> {result}'
    return fn


def template_function_2(result):
    def fn(part):
        return result
    fn.__doc__ = f'X -> {result}'
    return fn


def parse1(d):
    workflows, parts = d.split('\n\n')
    all_workflows = {}
    for workflow in workflows.split('\n'):
        name, instructions = workflow.split('{')
        instructions = instructions.strip('}').split(',')
        all_instructions = []
        for instruction in instructions:
            if ':' in instruction:
                test, result = instruction.split(':')
                if '<' in test:
                    attr, b = test.split('<')
                    b = int(b)
                    all_instructions.append(template_function(attr, operator.__lt__, b, result))
                else:
                    # '>'
                    attr, b = test.split('>')
                    b = int(b)
                    all_instructions.append(template_function(attr, operator.__gt__, b, result))
            else:
                all_instructions.append(template_function_2(instruction))
        all_workflows[name] = all_instructions

    all_parts = []
    for part in parts.split('\n'):
        this_part = {}
        for p in part.strip('{}').split(','):
            k, v = p.split('=')
            this_part[k] = int(v)
        all_parts.append(this_part)

    return all_workflows, all_parts


def parse2(d):
    all_workflows = {}
    workflows, S = d.split('\n\n')
    for workflow in workflows.split('\n'):
        key, rest = workflow.split('{')
        rest = rest.strip('}').split(',')
        parts = []
        for part in rest:
            if ':' in part:
                p1, p2 = part.split(':')
                if '<' in p1:
                    p1a, p1b = p1.split('<')
                    p1b = int(p1b)
                    parts.append((p1a, '<', p1b, p2))
                elif '>' in p1:
                    p1a, p1b = p1.split('>')
                    p1b = int(p1b)
                    parts.append((p1a, '>', p1b, p2))
                else:
                    raise ValueError
            else:
                parts.append(part)
        all_workflows[key] = parts
    return all_workflows


def part2(ranges, workflows):
    ranges = deepcopy(ranges)

    if 'R' in ranges:
        del ranges['R']
    AA = []

    keys = list(ranges.keys())
    for flow_id in keys:
        workflow = workflows[flow_id]
        while flow_id in ranges:
            for item in workflow:
                if isinstance(item, str):
                    thing = deepcopy(ranges[flow_id])

                    if item == 'A':
                        AA.append(thing)
                    else:
                        ranges[item] = thing

                    del ranges[flow_id]
                else:
                    key, op, n, new_flow_id = item
                    r = ranges[flow_id][key]

                    if n in r:
                        thing1 = deepcopy(ranges[flow_id])
                        thing2 = deepcopy(ranges[flow_id])
                        if op == '<':
                            thing1[key] = range(r.start, n)
                            thing2[key] = range(n, r.stop)

                            ranges[flow_id] = thing2

                            if new_flow_id == 'A':
                                AA.append(thing1)
                            else:
                                ranges[new_flow_id] = thing1
                        elif op == '>':
                            thing1[key] = range(r.start, n + 1)
                            thing2[key] = range(n + 1, r.stop)

                            ranges[flow_id] = thing1

                            if new_flow_id == 'A':
                                AA.append(thing2)
                            else:
                                ranges[new_flow_id] = thing2
                        else:
                            raise ValueError

                    else:
                        thing = deepcopy(ranges[flow_id])
                        ranges[new_flow_id] = thing
    return ranges, AA



def test_workflow(part, workflow):
    for instruction in workflow:
        result = instruction(part)
        if result is not None:
            return result


def test_part(part, workflows):
    workflow_name = 'in'
    while True:
        workflow = workflows[workflow_name]
        result = test_workflow(part, workflow)
        if result == 'A' or result == 'R':
            return result
        else:
            workflow_name = result


def part1(workflows, parts):
    accepted = []
    for part in parts:
        match test_part(part, workflows):
            case 'A':
                accepted.append(part)
            case 'R':
                pass
            case _:
                raise ValueError
    return sum(sum(a.values()) for a in accepted)


def main():
    d = get_input('19').strip()
    # d = TEST.strip()

    workflows, parts = parse1(d)
    p1 = part1(workflows, parts)
    print(p1)

    workflows = parse2(d)
    ranges = {
        'in': {
            'x': range(1, 4000+1),
            'm': range(1, 4000+1),
            'a': range(1, 4000+1),
            's': range(1, 4000+1)
        }
    }

    all_aa = []
    for _ in range(8):
        ranges, aa = part2(ranges, workflows)
        all_aa.extend(aa)

    m = 0
    for aa in all_aa:
        n = 1
        for r in aa.values():
            n *= len(r)
        m += n
    print(m)


if __name__ == '__main__':
    main()
