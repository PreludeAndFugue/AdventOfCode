#include <fstream>
#include <iostream>
#include <vector>

std::vector<int> get_ints(std::string filename) {
    std::vector<int> ns;
    int n;
    std::ifstream f { filename };

    if (!f) {
        std::cerr << "Error" << std::endl;
    }
    while (f) {
        f >> n;
        ns.push_back(n);
    }
    return ns;
}


std::vector<std::string> get_lines(std::string filename) {
    std::vector<std::string> lines;
    std::ifstream f { filename };
    std::string line;
    if (!f) {
        std::cerr << "Error" << std::endl;
    }
    while (f) {
        f >> line;
        lines.push_back(line);
    }
    return lines;
}
