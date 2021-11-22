#!python3

'''Day 17, part 1.'''

INPUT = '''43
3
4
10
21
44
4
6
47
41
34
17
17
44
36
31
46
9
27
38'''

containers = sorted((map(int, INPUT.strip().split('\n'))))
total = 150

test_containers = [20, 15, 10, 5, 5]
test_total = 25

def run(current, containers, total, results):
    for i, c in enumerate(containers):
        new_current = current + (c,)
        new_current_sum = sum(new_current)
        if new_current_sum > total:
            continue
        if new_current_sum == total:
            # yield new_current
            results.append(new_current)
        else:
            # rest = containers[:i] + containers[i + 1:]
            rest = containers[i + 1:]
            run(new_current, rest, total, results)

    return results


def test():
    cs = tuple(test_containers)
    results = run((), cs, test_total, [])

    print(results)
    print(len(results))


def main():
    cs = tuple(containers)
    results = run((), cs, total, [])

    print(results)
    print(len(results))

    # part 2

    min_len = min(len(result) for result in results)
    print(min_len)

    answer = sum(1 for result in results if len(result) == 4)
    print(answer)


if __name__ == '__main__':
    test()
    main()
