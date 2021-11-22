#!python3

'''Day 22, part 1.'''

from data_22 import grid, virus_position, test_grid, test_virus_position, Model


def test():
    model = Model(test_grid, test_virus_position)
    model.run(10_000_000)
    print(model.infect_count)


def main():
    model = Model(grid, virus_position)
    model.run(10_000_000)
    print(model.infect_count)


if __name__ == '__main__':
    # test()
    main()
