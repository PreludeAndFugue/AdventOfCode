#include <fstream>
#include <iostream>
#include <regex>
#include <sstream>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#include "basepath.cpp"

using namespace std;

typedef unordered_map<string, string> Passport;
typedef basic_istream<char> TextInput;

vector<string> REQUIRED_FIELDS { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" };
unordered_set<string> EYE_COLOUR { "amb", "blu", "brn", "gry", "grn", "hzl", "oth" };
regex HGT(R"(^(\d+)(\w{2})$)");
regex HCL(R"(^#[0-9a-f]{6}$)");
regex PID(R"(^\d{9}$)");

int part1(vector<Passport>);
int part2(vector<Passport>);
void test1();
void test2();
void test3();
vector<Passport> get_passports(TextInput&);
vector<string> make_records(TextInput&);
Passport make_map(string);
bool is_valid(Passport);
bool is_valid2(Passport);
bool has_missing_field(Passport);
bool is_valid_hgt(string);
bool is_valid_hcl(string);
bool is_valid_pid(string);


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

string TEST_INPUT_1 = R"(pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
)";


string TEST_INPUT_2 = R"(eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
)";


int main() {
    test1();
    test2();
    test3();

    ifstream f { base_path + "day04.txt" };
    vector<Passport> passports = get_passports(f);

    int p1 = part1(passports);
    cout << p1 << endl;

    int p2 = part2(passports);
    cout << p2 << endl;

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
    vector<Passport> parts = get_passports(os);
    assert(parts.size() == 4);
}


int part2(vector<Passport> passports) {
    int count { 0 };
    for (Passport p : passports) {
        if (is_valid2(p)) {
            count += 1;
        }
    }
    return count;
}


void test2() {
    stringstream os(TEST_INPUT_1);
    vector<Passport> passports = get_passports(os);
    for (Passport p : passports) {
        bool valid = is_valid2(p);
        assert(valid);
    }
}


void test3() {
    assert(EYE_COLOUR.find("gry") != EYE_COLOUR.end());
}


vector<Passport> get_passports(TextInput &s) {
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


bool is_valid2(Passport passport) {
    if (has_missing_field(passport)) {
        return false;
    }
    for (pair<string, string> p : passport) {
        string key = p.first;
        string value = p.second;
        if (key == "cid") {
            continue;
        } else if (key == "byr") {
            int y = stoi(value);
            if (y < 1920 || y > 2002) {
                return false;
            }
        } else if (key == "iyr") {
            int y = stoi(value);
            if (y < 2010 || y > 2020) {
                return false;
            }
        } else if (key == "eyr") {
            int y = stoi(value);
            if (y < 2020 || y > 2030) {
                return false;
            }
        } else if (key == "hgt") {
            if (!is_valid_hgt(value)) {
                return false;
            }
        } else if (key == "hcl") {
            if (!is_valid_hcl(value)) {
                return false;
            }
        } else if (key == "ecl") {
            if (EYE_COLOUR.find(value) == EYE_COLOUR.end()) {
                return false;
            }
        } else if (key == "pid") {
            if (!is_valid_pid(value)) {
                return false;
            }
        } else {
            assert(false);
        }
    }
    return true;
}


bool has_missing_field(Passport passport) {
    for (string field : REQUIRED_FIELDS) {
        if (passport.find(field) == passport.end()) {
            return true;
        }
    }
    return false;
}


bool is_valid_hgt(string value) {
    smatch m;
    if (!regex_match(value, m, HGT)) {
        return false;
    }
    int q = stoi(m[1].str());
    string u = m[2].str();
    if (u == "cm") {
        return (q >= 150 && q <= 193);
    } else if (u == "in") {
        return (q >= 59 && q <= 76);
    } else {
        return false;
    }
}


bool is_valid_hcl(string value) {
    return regex_match(value, HCL);
}


bool is_valid_pid(string value) {
    return regex_match(value, PID);
}
