#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

#include "basepath.cpp"
#include "inputhelpers.cpp"

typedef std::string Pass;
typedef std::vector<std::string> Passes;
typedef int SeatId;

void part1();
void test1();
Passes get_passes();
const SeatId get_seat_id(Pass);
const int get_row(Pass);
const int get_column(Pass);

const Passes TESTS {
    "FBFBBFFRLR",
    "BFFFBBFRRR",
    "FFFBBBFRRR",
    "BBFFBBFRLL"
};

int main() {
    // test1();
    part1();

    return 0;
}


void part1() {
    Passes passes = get_passes();
    std::vector<SeatId> seat_ids;
    for (Pass pass : passes) {
        SeatId seat_id = get_seat_id(pass);
        seat_ids.push_back(seat_id);
    }
    int max = *std::max_element(seat_ids.begin(), seat_ids.end());
    std::cout << "Part 1 " << max << std::endl;
}


Passes get_passes() {
    return get_lines(base_path + "day05.txt");
}


void test1() {
    for (string t : TESTS) {
        std::cout << t << ' ' << get_seat_id(t) << std::endl;
    }
}


const SeatId get_seat_id(std::string code) {
    const int row = get_row(code);
    const int column = get_column(code);
    return 8 * row + column;
}


const int get_row(std::string code) {
    int row { 0 };
    for (int i = 0; i < 7; i++) {
        const char test = code[i];
        if (test == 'F') {
            row = row << 1;
        } else if (test == 'B') {
            row = (row << 1) + 1;
        } else {
            std::cout << "row char error " << test << std::endl;
        }
    }
    return row;
}


const int get_column(std::string code) {
    int column { 0 };
    for (int i = 7; i < 10; i++) {
        const char test = code[i];
        if (test == 'R') {
            column = (column << 1) + 1;
        } else if (test == 'L') {
            column = column << 1;
        } else {
            std::cout << "column char error " << code[i] << std::endl;
        }
    }
    return column;
}