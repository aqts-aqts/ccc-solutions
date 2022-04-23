#include <bits/stdc++.h>
using namespace std;

int main() {
    int grid[4] = {1, 2, 3, 4};
    string actions;
    cin >> actions;
    int hs = 0;
    int vs = 0;
    for (char c : actions) {
        if (c == 'H') {
            hs++;
        } else {
            vs++;
        }
    }
    if (hs % 2 == 0 && vs % 2 == 0)
        cout << "1 2\n3 4";
    else if (hs % 2 == 1 && vs % 2 == 0)
        cout << "3 4\n1 2";
    else if (hs % 2 == 0 && vs % 2 == 1)
        cout << "2 1\n4 3";
    else
        cout << "4 3\n2 1";

}