#include <bits/stdc++.h>
using namespace std;

string cyclic(string s) {
    string n = "";
    for (int i = 1; i < s.length(); i++) {
        n += s[i];
    }
    n += s[0];
    return n;
}

int main() {
    map<string, int> cyclics;
    string t, s;
    bool found = false;
    cin >> t;   
    cin >> s;
    cin.ignore();

    for (int i = 0; i <= t.length() - s.length(); i++) {
        cyclics[t.substr(i, s.length())] = i;
    }

    for (int i = 0; i < s.length(); i++) {
        if (cyclics.count(s) > 0) {
            found = true;
            break;
        }

        s = cyclic(s);
    }


    if (found) {
        cout << "yes";
    } else {
        cout << "no";
    }
}