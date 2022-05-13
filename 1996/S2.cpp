#include <bits/stdc++.h>
using namespace std;

string subtract(string s1, string s2) {
    string r = "";
    int c = 0;
    string s(s1.length() - s2.length(), '0');
    s2 = s + s2;
    for (int i = s2.length() - 1; i >= 0; i--) {
        int d1 = s1[i] - '0';
        int d2 = s2[i] - '0';
        int result = d1 - d2 - c;
        if (result < 0) {
            c = 1;
            result += 10;
        } else c = 0;
        r = to_string(result) + r;
    }
    if (c == 1) r = '1' + r;
    r.erase(0, min(r.find_first_not_of('0'), r.size() - 1));
    return r;
}

int main() {
  ios_base::sync_with_stdio(false);
  int t;
  cin >> t;
  for (int c = 0; c < t; c++) {
    string num;
    cin >> num;
    string calc = num;
    bool valid = true;
    bool printed = false;
    if (calc.size() <= 2 && stoi(calc) <= 11) {
      valid = false;
      cout << calc << "\n";
      printed = true;
    }
    while (calc.size() > 2) {
      cout << calc << "\n";
      string end;
      end.push_back(calc.back());
      calc.resize(calc.size() - 1);
      calc = subtract(calc, end);
    }
    if (!printed) cout << calc << "\n";
    if (stoi(calc) % 11 == 0) valid = true;
    else valid = false;
    if (!valid) cout << "The number " + num + " is not divisible by 11." << "\n";
    else cout << "The number " + num + " is divisible by 11." << "\n";
    if (c != t - 1) cout << "\n";
  }
}
