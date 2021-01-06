#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

#include "basepath.cpp"

using namespace std;

void test1();
int part1(vector<string>);
vector<string> make_map();
int tree_count(vector<string>, int);

string TEST_INPUT = R"(..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#)";


int main() {
    vector<string> map = make_map();

    test1();
    int p1 = part1(map);

    cout << p1 << endl;
    return 0;
}


int tree_count(vector<string> map, int offset) {
    int width = map.at(0).size();
    int count{ 0 };
    int column{ 0 };
    for (int i = 0; i < map.size(); i++) {
        if (map.at(i).at(column) == '#') {
            count += 1;
        }
        column = (column + offset) % width;
    }
    return count;
}


vector<string> make_map() {
    ifstream f{ base_path + "day03.txt" };
    string line;
    vector<string> map;
    while (getline(f, line)) {
        map.push_back(line);
    }
    return map;
}


int part1(vector<string> map) {
    return tree_count(map, 3);
}


void test1() {
    stringstream os(TEST_INPUT);
    vector<string> map;
    string line;
    while (getline(os, line)) {
        map.push_back(line);
    }
    int c = tree_count(map, 3);
    assert(c == 7);
}
