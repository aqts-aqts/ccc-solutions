#include <bits/stdc++.h>
using namespace std;

string formatString(string str) {
    string newString;
    for (int i = 0; i < str.size(); i++) {
        newString.push_back('|');
        newString.push_back(str[i]);
    }
    newString.push_back('|');
    return newString;
}

string findLongestPalindromicSubstring(string str) {
    str = formatString(str);
    int LPS[str.size()] = {0};
    int c = 0; 
    int longest = 0;
    for (int i = 0; i < str.size(); i++) {
        int ss = 2 * c - i;
        if (longest > i) 
            LPS[i] = min(longest - i, LPS[ss]);
        else
            LPS[i] = 0;
        
        try {
            while (str[i + 1 + LPS[i]] == str[i - 1 - LPS[i]])
                LPS[i]++;
        } catch(...) {}
        if (i + LPS[i] > longest) {
            c = i;
            longest = i + LPS[i];
        }
    }
    longest = *max_element(LPS, LPS + str.size());
    c = distance(LPS, find(LPS, LPS + str.size(), longest));
    return str.substr(c - longest, longest * 2);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int t; 
    cin >> t;
    for (int c = 0; c < t; c++) {
        string str;
        cin >> str;
        string temp = str;
        reverse(temp.begin(), temp.end());
        if (str == temp) {
            cout << str << endl;
            cout << str.size() << endl;
            continue;
        }

        str = findLongestPalindromicSubstring(str);
        int size = 0;
        for (char c: str) {
            if (c != '|') {
                cout << c;
                size++;
            }
        }
        cout << endl << size << endl;
    }
}