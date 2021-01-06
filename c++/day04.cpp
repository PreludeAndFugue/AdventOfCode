#include <fstream>
#include <iostream>
#include <sstream>
#include <unordered_map>
#include <vector>

#include "basepath.cpp"

using namespace std;

typedef unordered_map<string, string> Passport;
typedef basic_istream<char> TextInput;

int part1(vector<Passport>);
void test1();
vector<Passport> get_passport_records(TextInput&);
vector<string> make_records(TextInput&);
Passport make_map(string);
bool is_valid(Passport);


string TEST_INPUT = R"(ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
)";


int main() {
    test1();

    ifstream f { base_path + "day04.txt" };
    vector<Passport> passports = get_passport_records(f);

    int p1 = part1(passports);
    cout << p1 << endl;

    return 0;
}


int part1(vector<Passport> passports) {
    int count { 0 };
    for (Passport passport : passports) {
        if (is_valid(passport)) {
            count += 1;
        }
    }
    return count;
}


void test1() {
    stringstream os(TEST_INPUT);
    vector<Passport> parts = get_passport_records(os);
    assert(parts.size() == 4);
}


vector<Passport> get_passport_records(TextInput &s) {
    vector<string> records = make_records(s);
    vector<Passport> result;
    for (string record : records) {
        Passport p = make_map(record);
        result.push_back(p);
    }
    return result;
}


vector<string> make_records(TextInput &s) {
    string line;
    string full_line;
    vector<string> parts;
    while (getline(s, line)) {
        if (line == "") {
            parts.push_back(full_line);
            full_line = "";
        } else {
            if (full_line == "") {
                full_line = line;
            } else {
                full_line += " " + line;
            }
        }
    }
    parts.push_back(full_line);
    return parts;
}


Passport make_map(string line) {
    Passport passport;
    istringstream input(line);
    while (true) {
        string part;
        input >> part;
        if (part == "") {
            break;
        }
        int p = part.find(":");
        string key = part.substr(0, p);
        string value = part.substr(p + 1);
        passport[key] = value;
    }
    return passport;
}


bool is_valid(Passport passport) {
    if (passport.size() == 8) {
        return true;
    } else if (passport.size() == 7) {
        auto s = passport.find("cid");
        return (s == passport.end());
    } else {
        return false;
    }
}
