#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

#include "basepath.cpp"

using namespace std;

void test1();
int part1(vector<string>);
int64_t part2(vector<string>);
vector<string> make_map();
int tree_count(vector<string>, int, int);

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

    int64_t p2 = part2(map);
    cout << p2 << endl;
    return 0;
}


int tree_count(vector<string> map, int right, int down) {
    int width = map.at(0).size();
    int count { 0 };
    int column { 0 };
    for (int i = 0; i < map.size(); i = i + down) {
        if (map.at(i).at(column) == '#') {
            count += 1;
        }
        column = (column + right) % width;
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
    return tree_count(map, 3, 1);
}


int64_t part2(vector<string> map) {
    vector<pair<int, int>> pairs{
        make_pair(1, 1), make_pair(3, 1), make_pair(5, 1), make_pair(7, 1),
        make_pair(1, 2)
    };
    int c;
    int64_t t { 1 };
    for (pair<int, int> p: pairs) {
        c = tree_count(map, p.first, p.second);
        t = t * static_cast<int64_t>(c);
    }
    return t;
}


void test1() {
    stringstream os(TEST_INPUT);
    vector<string> map;
    string line;
    while (getline(os, line)) {
        map.push_back(line);
    }
    int c = tree_count(map, 3, 1);
    assert(c == 7);
}
