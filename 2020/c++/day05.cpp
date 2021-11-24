#include <iostream>
#include <string>
#include <vector>

void test1();
const int get_seat_id(std::string);
const int get_row(std::string);
const int get_column(std::string);

const std::vector<std::string> TESTS {
    "FBFBBFFRLR",
    "BFFFBBFRRR",
    "FFFBBBFRRR",
    "BBFFBBFRLL"
};

int main() {
    test1();

    return 0;
}


void test1() {
    for (auto t : TESTS) {
        std::cout << t << ' ' << get_seat_id(t) << std::endl;
    }
}


const int get_seat_id(std::string code) {
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