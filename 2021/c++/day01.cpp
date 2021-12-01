#include <iostream>
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


int window_sum(std::vector<int> values, int index, int window_size) {
    int sum;
    std::vector<int> window;
    for (int i = 0; i < window_size; i++) {
        int n = values.at(index + i);
        sum = sum + n;
    }
    return sum;
}


int part1(std::vector<int> depths) {
    int count = 0;
    int size = depths.size();
    for (int i = 0; i < size - 1; i++) {
        int m = depths.at(i);
        int n = depths.at(i + 1);
        if (n > m) {
            count++;
        }
    }
    return count;
}


int part2(std::vector<int> depths) {
    int count = 0;
    int size = depths.size();
    for (int i = 0; i < size - 3; i++) {
        int m = window_sum(depths, i, 3);
        int n = window_sum(depths, i + 1, 3);
        if (n > m) {
            count++;
        }
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
