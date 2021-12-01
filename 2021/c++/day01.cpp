#include <iostream>
#include <limits>
#include <vector>

#include "basepath.cpp"
#include "inputhelpers.cpp"


std::vector<int> TEST01 = {
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
};


int part1(std::vector<int> depths) {
    int count = 0;
    int previous = std::numeric_limits<int>::max();
    for (int n : depths) {
        if (n > previous) {
            count++;
        }
        previous = n;
    }
    return count;
}

// When comparing the window sum, only need to compare the first and last values.
// w1 = a1 + a2 + a3
// w2 = a2 + a3 + a4
// w2 - w1 = a2 + a3 + a4 - a1 - a2 - a3 = a4 - a1
int part2(std::vector<int> depths) {
    int count = 0;
    int size = depths.size();
    int previous = depths.at(0);
    int n;
    for (int i = 3; i < size; i++) {
        n = depths.at(i);
        if (n > previous) {
            count++;
        }
        previous = depths.at(i - 2);
    }
    return count;
}


int main() {
    std::string path = source_path + "day01.txt";
    std::vector<int> depths = get_ints(source_path + "day01.txt");

    int t1 = part1(TEST01);
    assert(t1 == 7);

    int p1 = part1(depths);

    int t2 = part2(TEST01);
    assert(t2 == 5);

    int p2 = part2(depths);

    std::cout << "Part 1: " << p1 << std::endl;
    std::cout << "Part 2: " << p2 << std::endl;
    return 0;
}
