#include <bits/stdc++.h>
using namespace std;

int value(char perm[10], string word, int layer, int num) {
    int index = word.length() - layer;
    if (index < 0) {return 0;}
    char letter = word[index];
    for (int i = 0; i < 10; i++) {
        if (perm[i] == letter) 
            return i;
    }
    if (perm[num] == ' ') {
        perm[num] = letter;
        return num;
    }
    return -1;
}

bool solve(string word1, string word2, string word3, char perm[10], int layer, int carry) {
    bool* visited = new bool[1000];
    char current[10];
    memset(visited, false, 1000 * sizeof(bool));
    memcpy(current, perm, 10 * sizeof(char));
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            for (int k = 0; k < 10; k++) {
                int num1 = value(perm, word1, layer, i);
                int num2 = value(perm, word2, layer, j);
                int num3 = value(perm, word3, layer, k);
                int val = num1 * 100 + num2 * 10 + num3;  
                if (num1 >= 0 && num2 >= 0 && num3 >= 0 && visited[val] != 1) {
                    int sum = carry + num1 + num2 - num3;
                    if (sum % 10 == 0) {
                        if (layer == word3.length()) {
                            if (sum == 0 && num3 > 0) {
                                for (int x = word1.length(); x > 0; x--)
                                    cout << value(perm, word1, x, 0);
                                cout << endl;
                                for (int x = word2.length(); x > 0; x--) 
                                    cout << value(perm, word2, x, 0);
                                cout << endl;
                                for (int x = word3.length(); x > 0; x--) 
                                    cout << value(perm, word3, x, 0);
                                cout << endl;
                                return true;
                            }
                        } else if (solve(word1, word2, word3, perm, layer + 1, sum / 10))
                            return true;
                    }
                    visited[val] = true;
                }
                memcpy(perm, current, 10 * sizeof(char));
            }
        }
    }
    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    for (int c = 0; c < t; c++) {
        string word1;
        string word2;
        string word3;
        cin >> word1;
        cin >> word2;
        cin >> word3;
        char perm[10] = {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};
        solve(word1, word2, word3, perm, 1, 0);
    }
}