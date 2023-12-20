
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


def parse(d):
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


def test(part, workflow):
    for instruction in workflow:
        result = instruction(part)
        if result is not None:
            return result


def part1(workflows, parts):
    accepted = []
    for part in parts:
        # print(part)
        workflow_name = 'in'
        while True:
            workflow = workflows[workflow_name]
            result = test(part, workflow)
            # print(result)
            # input()
            if result == 'A':
                accepted.append(part)
                break
            elif result == 'R':
                break
            else:
                workflow_name = result
    return sum(sum(a.values()) for a in accepted)


def main():
    d = get_input('19').strip()
    # d = TEST.strip()
    workflows, parts = parse(d)

    p1 = part1(workflows, parts)
    print(p1)


if __name__ == '__main__':
    main()
