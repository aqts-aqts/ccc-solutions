#include <bits/stdc++.h>
using namespace std;
#define fast ios_base::sync_with_stdio(false); cin.tie(NULL);

string add(string s1, string s2) {
    string r = "";
    int c = 0;
    string s(s1.length() - s2.length(), '0');
    s2 = s + s2;
    for (int i = s2.length() - 1; i >= 0; i--) {
        int d1 = s1[i] - '0';
        int d2 = s2[i] - '0';
        int result = d1 + d2 + c;
        if (result >= 10) {
            c = 1;
            result -= 10;
        } else c = 0;
        r = to_string(result) + r;
    }
    if (c == 1) r = '1' + r;
    return r;
}

unordered_map<int, string> visited;
string fib(int n) {
    if (visited.find(n) != visited.end()) return visited[n];
    if (n == 1 or n == 0) return to_string(n);
    visited[n] = add(fib(n - 1), fib(n - 2));
    return visited[n];
}

int main() {
    fast
    int n;
    cin >> n;
    while (n != 0) {
        cout << fib(n) << '\n';
        cin >> n;
    }
}