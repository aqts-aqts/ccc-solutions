#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    string coordinates;
    int x, y;
    int x_min = 100;
    int y_min = 100;
    int x_max = 0;
    int y_max = 0;
    for (int i = 0; i < n; i++) {
        cin >> coordinates;
        auto pos = coordinates.find(",");
        x = stoi(coordinates.substr(0, pos));
        y = stoi(coordinates.substr(pos + 1));

        x_min = min(x_min, x);
        y_min = min(y_min, y);
        x_max = max(x_max, x);
        y_max = max(y_max, y);       
    }
    cout << x_min - 1 << "," << y_min - 1 << endl;
    cout << x_max + 1 << "," << y_max + 1 << endl;
    return 0;
}
