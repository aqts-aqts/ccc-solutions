#include <iostream>
#include <string>
using namespace std;

string a;

int split(string str) {
    string w = "";
    int j = 0;
    int k = 0;
    for (int i = 0; i < str.length(); i++) {
        if (str[i] == ' ') {
            k = stoi(w);
            w = "";
        } else {
            w = w + str[i];
        }
        
    }
    a = w;
    return k;
}

int main() {
    int l;
    cin >> l;
    string actions[l];
    cin.ignore();
    for (int i = 0; i < l; i++) {
        getline(cin, actions[i]);
    }

    for (int i = 0; i < l; i++) {
        string action = actions[i];
        for (int i = 0; i < split(action); i++) {
            cout << a;
        }
        cout << endl;
    }
}