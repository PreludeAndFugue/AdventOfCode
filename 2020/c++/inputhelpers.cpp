#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

vector<int> get_ints(string filename) {
    vector<int> ns;
    int n;
    ifstream f { filename };

    if (!f) {
        cerr << "Error" << endl;
    }
    while (f) {
        f >> n;
        ns.push_back(n);
    }
    return ns;
}
