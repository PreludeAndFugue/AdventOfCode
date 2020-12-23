#!python3


INPUT = '792845136'
TEST_INPUT = '389125467'


class Node(object):
    def __init__(self, label):
        self.label = label
        self.next = None


    def __repr__(self):
        next_label = self.next.label if self.next else '?'
        return f'Node({self.label}, next: {next_label})'


class CircularLinkedList(object):
    def __init__(self, current, size):
        self.current = current
        self.size = size


    def move(self):
        removed_start = self.current.next
        removed_end = removed_start.next.next
        # removed_end.next = None
        after_removed = removed_end.next
        self.current.next = after_removed

        destination = self._get_destination_cup(removed_start)
        after_destination = destination.next
        destination.next = removed_start
        removed_end.next = after_destination

        self.current = self.current.next


    def get_node_with_label(self, label):
        node = self.current
        while node.label != label:
            node = node.next
        return node


    def _get_destination_cup(self, removed_start):
        destination_label = self._get_destination_cup_label(removed_start)
        # print('destination label', destination_label)
        node = self.current
        while node.label != destination_label:
            node = node.next
        return node


    def _get_destination_cup_label(self, removed_start):
        removed_labels = [
            removed_start.label,
            removed_start.next.label,
            removed_start.next.next.label
        ]
        i = (self.current.label - 2) % self.size
        while (i + 1) in removed_labels:
            i = (i - 1) % self.size
        return i + 1


    @classmethod
    def make_with_labels(cls, labels):
        current = Node(labels[0])
        current_node = current
        for i in labels[1:]:
            next_node = Node(i)
            current_node.next = next_node
            current_node = next_node
        next_node.next = current
        return cls(current, len(labels))


    @classmethod
    def make_with_string_labels(cls, labels):
        labels = list(map(int, list(labels)))
        return cls.make_with_labels(labels)


    def __repr__(self):
        current_label = self.current.label
        labels = [current_label]
        next_node = self.current.next
        while next_node.label != current_label:
            labels.append(next_node.label)
            next_node = next_node.next
        return repr(labels)


def _part1(cll):
    '''Get the labels in order after label 1.'''
    n1 = cll.get_node_with_label(1)
    node = n1.next
    labels = []
    while node.label != 1:
        labels.append(node.label)
        node = node.next
    return ''.join(map(str, labels))


def test1():
    cll = CircularLinkedList.make_with_string_labels(TEST_INPUT)
    for _ in range(10):
        cll.move()
    x = _part1(cll)
    assert x == '92658374'


def test2():
    cll = CircularLinkedList.make_with_string_labels(TEST_INPUT)
    for _ in range(100):
        cll.move()
    x = _part1(cll)
    assert x == '67384529'


def part1():
    cll = CircularLinkedList.make_with_string_labels(INPUT)
    for _ in range(100):
        # print(f'-- move {i} --')
        # print(cll)
        cll.move()
    x = _part1(cll)
    return x


def part2():

    MAX = 50
    MOVES = 100

    start_labels = list(map(int, list(INPUT)))
    # print(start_labels)
    new_start = max(start_labels) + 1
    all_labels = start_labels + list(range(new_start, MAX + 1))
    # print('len all labels', len(all_labels))
    cll = CircularLinkedList.make_with_labels(all_labels)
    # print('cll.size', cll.size)
    # print('starting moves')
    for _ in range(MOVES):
        print(cll)
        cll.move()


def main():
    # test1()
    # test2()

    # p = part1()
    # print(p)

    p = part2()
    print(p)


if __name__ == "__main__":
    main()
    # import timeit
    # x = timeit.timeit('main()', setup='from __main__ import main', number=1)
    # print(x)
