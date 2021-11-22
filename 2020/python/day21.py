#!python3

from collections import Counter, defaultdict
from itertools import chain

INPUT = 'day21.txt'

TEST_INPUT = '''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
'''


def make_food(input):
    for line in input.strip().split('\n'):
        ingredients, allergens = line.strip().split(' (contains ')
        ingredients = ingredients.split(' ')
        allergens = allergens.strip(')').split(', ')
        yield Food(ingredients, allergens)


class Food(object):
    def __init__(self, ingredients, allergens):
        self.ingredients = ingredients
        self.allergens = set(allergens)


    def check_ingredient_allergen_map(self, ingredient_allergen_map):
        test_allergens = set()
        for ingredient in self.ingredients:
            if ingredient in ingredient_allergen_map:
                test_allergens.add(ingredient_allergen_map[ingredient])
        x = test_allergens >= self.allergens
        return x


    def __repr__(self):
        return f'Food({self.ingredients}, {self.allergens})'


def find_unique_max(allergen_helper):
    '''Find the first allergen that has a unique ingredient with the max count.'''
    for allergen, counts in allergen_helper.items():
        c = Counter(v for v in counts.values())
        max_c = max(k for k in c.keys())
        max_c_count = c[max_c]
        if max_c_count == 1:
            ingredient = [k for k, v in counts.items() if v == max_c]
            assert len(ingredient) == 1
            return allergen, ingredient[0]


def do_all(food):
    all_allergens = sorted(set(chain(*[f.allergens for f in food])))
    all_ingredients = set(chain(*[f.ingredients for f in food]))

    allergen_helper = {}
    for allergen in all_allergens:
        d = defaultdict(int)
        for f in food:
            if allergen not in f.allergens:
                continue
            for i in f.ingredients:
                d[i] += 1
        allergen_helper[allergen] = d

    found = {}
    while len(found) < len(all_allergens):
        a, i = find_unique_max(allergen_helper)
        found[i] = a
        del allergen_helper[a]
        for v in allergen_helper.values():
            if i in v:
                del v[i]

    unused_ingredients = all_ingredients - set([k for k in found.keys()])

    count_unused = 0
    for i in unused_ingredients:
        for f in food:
            if i in f.ingredients:
                count_unused += 1

    # part 2
    found1 = {v: k for k, v in found.items()}
    fkeys = sorted(k for k in found1.keys())
    fvalues = ','.join(found1[a] for a in fkeys)

    return count_unused, fvalues


def test1():
    food = list(make_food(TEST_INPUT))
    return do_all(food)


def part1():
    food = list(make_food(open(INPUT, 'r').read()))
    return do_all(food)


def main():
    t1, t2 = test1()
    assert t1 == 5
    assert t2 == 'mxmxvkd,sqjhc,fvjkl'

    p1, p2 = part1()
    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
