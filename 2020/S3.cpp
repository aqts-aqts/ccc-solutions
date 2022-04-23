#include <bits/stdc++.h>
using namespace std;

bool permutation(unordered_map<char, int> needle, unordered_map<char, int> haystack) {
    for (int i = 0; i < 26; i++) {
        char let = 'a' + i;
        if (needle[let] != haystack[let])
            return false;
    }

    return true;
}

int findPermutations(string needle, string haystack) {
    int need = needle.length();
    int hay = haystack.length();

    unordered_map<char, int> n;
    unordered_map<char, int> h;
    for (char c: needle)
        n[c]++;

    int perms = 0;
    map<string, bool> visited;
    for (int i = 0; i < hay - need + 1; i++) {
        string substr = haystack.substr(i, need);
        if (i == 0) {
            for (char c: substr)
                h[c]++;
        } else {
            char left = haystack[i - 1];
            char right = haystack[i + substr.length() - 1];
            h[left]--;
            h[right]++;
        }

        if (permutation(n, h) && !visited[substr]) {
            visited[substr] = true;
            perms++;
        }
    }

    return perms;
}

int main() {
    string needle, haystack;
    cin >> needle;
    cin >> haystack;
    
    cout << findPermutations(needle, haystack);
}