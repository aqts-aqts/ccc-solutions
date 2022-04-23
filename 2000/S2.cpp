#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    vector<double> streams;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        streams.push_back(temp);
    }

    int num;
    cin >> num;
    while (num != 77) {
        if (num == 99) {
            double n1, n2;
            cin >> n1;
            cin >> n2;
            double h = streams[n1-1];
            streams[n1 - 1] = h * (n2 / 100);
            auto pos = streams.begin() + n1;
            streams.insert(pos, h - h * (n2 / 100));
        } else if (num == 88) {
            double n3, n4;
            cin >> n3;
            n4 = streams[n3-1];
            auto it = streams.begin() + n3 - 1;
            streams.erase(it);
            streams[n3-1] += n4;
        }
        /*
        for (int i = 0; i < streams.size(); i++) {
            cout << streams[i] << " ";
        }
        */

        cin >> num;
    }

    for (int i = 0; i < streams.size(); i++) {
        cout << round(streams[i]) << " ";
    }
}