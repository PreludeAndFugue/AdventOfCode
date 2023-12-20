
from collections import Counter
from copy import deepcopy
import operator

from help import get_input


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
            # print(part)
            if ':' in part:
                p1, p2 = part.split(':')
                # print(p1, p2)
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
        print(key, parts)
        all_workflows[key] = parts
    return all_workflows


def part2(ranges, workflows):
    ranges = deepcopy(ranges)

    # new_test = {}
    keys = list(ranges.keys())
    for flow_id in keys:
        print('processing key', flow_id)
        while flow_id in ranges:
            workflow = workflows[flow_id]
            for item in workflow:
                if isinstance(item, str):
                    print('map to new key')
                    # print(item)
                    # v = test[flow_id]
                    # new_test[item] = v
                    thing = deepcopy(ranges[flow_id])
                    ranges[item] = thing
                    del ranges[flow_id]
                    pass
                else:
                    print('map ranges to new keys')
                    key, op, n, new_flow_id = item
                    # print(key, op, n, new_flow_id)
                    r = ranges[flow_id][key]
                    # print(r)
                    if op == '<':
                        if n in r:
                            # print('n in r', n, r)
                            r1 = range(r.start, n)
                            r2 = range(n, r.stop)
                            # print(r1, r2)
                            thing1 = deepcopy(ranges[flow_id])
                            thing1[key] = r1
                            ranges[new_flow_id] = thing1

                            thing2 = deepcopy(ranges[flow_id])
                            thing2[key] = r2
                            ranges[flow_id] = thing2
                        else:
                            ranges[new_flow_id] = ranges[flow_id]
                    elif op == '>':
                        if n in r:
                            r1 = range(r.start, n)
                            r2 = range(n, r.stop)

                            thing1 = deepcopy(ranges[flow_id])
                            thing1[key] = r1
                            ranges[flow_id] = thing1

                            thing2 = deepcopy(ranges[flow_id])
                            thing2[key] = r2
                            ranges[new_flow_id] = thing2
                        else:
                            ranges[new_flow_id] = ranges[flow_id]
                    else:
                        raise ValueError

    # print(ranges)
    return ranges



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


def extract(ranges):
    aa = 0
    rr = 0
    if 'R' in ranges:
        rr = 1
        r = ranges['R']
        print('R', r)
        for value in r.values():
            l = len(value)
            rr *= l
        del ranges['R']

    if 'A' in ranges:
        aa = 1
        r = ranges['A']
        print('A',  r)
        for value in r.values():
            l = len(value)
            aa *= l
        del ranges['A']

    return deepcopy(ranges), aa, rr


def main():
    d = get_input('19').strip()
    # d = TEST.strip()

    # workflows, parts = parse1(d)
    # p1 = part1(workflows, parts)
    # print(p1)

    workflows = parse2(d)
    ranges = {
        'in': {
            'x': range(1, 4000+1),
            'm': range(1, 4000+1),
            'a': range(1, 4000+1),
            's': range(1, 4000+1)
        }
    }

    total = 0
    other = 0
    for _ in range(6):
        ranges = part2(ranges, workflows)
        print(ranges)
        ranges, n, m = extract(ranges)
        total += n
        other += m
        print(ranges)
        print(n)
        print(m)

    print('total')
    print(total)
    print('other', other)
    print('total + other', total + other)
    a = 167409079868000
    b = 4_000 * 4_000 * 4_000 * 4_000
    print(a)
    print(b)
    print(b - a)


if __name__ == '__main__':
    main()
