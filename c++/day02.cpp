#include <fstream>
#include <iostream>
#include <regex>
#include <sstream>

#include "basepath.cpp"

using namespace std;

struct Password {
    int lower;
    int upper;
    char c;
    string password;
};

Password make_password(string, regex);
vector<Password> make_passwords();
bool is_valid(Password);
int part1(vector<Password>);
int part2(vector<Password>);


int main() {
    auto passwords = make_passwords();
    int p1 = part1(passwords);
    int p2 = part2(passwords);
    cout << p1 << endl;
    cout << p2 << endl;
}


Password make_password(string line, regex password_regex) {
    smatch m;
    regex_match(line, m, password_regex);
    int lower = stoi(m[1].str());
    int upper = stoi(m[2].str());
    char c = m[3].str()[0];
    string password = m[4].str();
    return Password{ lower, upper, c, password };
}


vector<Password> make_passwords() {
    ifstream f { base_path + "day02.txt" };
    regex password_regex = regex(R"(^(\d+)-(\d+) (\w): (\w+)$)");
    vector<Password> passwords;
    string line;
    while (getline(f, line)) {
        Password p = make_password(line, password_regex);
        passwords.push_back(p);
    }
    return passwords;
}


bool is_valid(Password password) {
    int count = 0;
    for (char c : password.password) {
        if (c == password.c) {
            count += 1;
        }
    }
    return password.lower <= count && count <= password.upper;
}


bool is_valid2(Password password) {
    bool a = password.password.at(password.lower - 1) == password.c;
    bool b = password.password.at(password.upper - 1) == password.c;
    return (a != b);
}


int part1(vector<Password> passwords) {
    int count = 0;
    for (Password p : passwords) {
        if (is_valid(p)) {
            count += 1;
        }
    }
    return count;
}


int part2(vector<Password> passwords) {
    int count = 0;
    for (Password p : passwords) {
        if (is_valid2(p)) {
            count += 1;
        }
    }
    return count;
}