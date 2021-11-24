// clang++ -std=c++20 -Wall day01.cpp -o build/day01

#include <iostream>
#include <unordered_set>

#include "basepath.cpp"
#include "inputhelpers.cpp"

using namespace std;

int part1(vector<int>);
int part2(vector<int>);


int main() {
    vector<int> ns = get_ints(base_path + "day01.txt");
    cout << part1(ns) << endl;
    cout << part2(ns) << endl;
}


int part1(vector<int> ns) {
    unordered_set<int> inverses;
    int s = ns.size();
    for (int i = 0; i < s; i++) {
        int n = ns.at(i);
        auto f = inverses.find(n);
        if (f != inverses.end()) {
            return n * (2020 - n);
        } else {
            inverses.insert(2020 - n);
        }
    }
    return 0;
}


int part2(vector<int> ns) {
    int s = ns.size();
    for (int i = 0; i < s; i++) {
        int n_i = ns.at(i);
        for (int j = i + 1; j < s; j++) {
            int n_j = ns.at(j);
            int partial = n_i + n_j;
            if (partial >= 2020) {
                continue;
            }
            for (int k = j + 1; k < s; k++) {
                int n_k = ns.at(k);
                if (partial + n_k == 2020) {
                    return n_i * n_j * n_k;
                }
            }
        }
    }
    return 0;
}