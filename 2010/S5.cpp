#include <bits/stdc++.h>

using namespace std;

class Node {
public:
    Node *left, *right;
    int value;
    vector<int> nutrients;

    Node(Node *left, Node *right, int value = 0) : left(left), right(right), value(value) {}
};

string trim(const string& str) {
    size_t first = str.find_first_not_of(" \n\r\t");
    size_t last = str.find_last_not_of(" \n\r\t");

    if (first == string::npos || last == string::npos)
        return "";
    
    return str.substr(first, (last - first + 1));
}

Node* createNode(string s, int x) {
    s = trim(s);
    if (s[0] != '(') {
        return new Node(nullptr, nullptr, stoi(s));
    } else {
        string inner = trim(s.substr(1, s.size() - 2));
        int i = 0, count = 0;
        if (inner[0] == '(') {
            count = 1;
            i = 1;
            while (count > 0) {
                if (inner[i] == '(') count++;
                else if (inner[i] == ')') count--;
                i++;
            }
        } else {
            i = inner.find(' ');
        }
        Node *left = createNode(inner.substr(0, i), x);
        Node *right = createNode(inner.substr(i + 1), x);
        return new Node(left, right);
    }
}

void solve(Node* node, int x) {
    node->nutrients.resize(x + 1);
    if (node->left == nullptr && node->right == nullptr) {
        for (int i = 0; i <= x; ++i) {
            node->nutrients[i] = node->value + i;
        }
    } else {
        solve(node->left, x);
        vector<int> left(x + 1, 0);
        for (int i = 0; i <= x; ++i) {
            int maxLeft = 0;
            for (int j = 0; j <= i; ++j) {
                maxLeft = max(maxLeft, min((1 + j) * (1 + j), node->left->nutrients[i - j]));
            }
            left[i] = maxLeft;
        }

        solve(node->right, x);
        vector<int> right(x + 1, 0);
        for (int i = 0; i <= x; ++i) {
            int maxRight = 0;
            for (int j = 0; j <= i; ++j) {
                maxRight = max(maxRight, min((1 + j) * (1 + j), node->right->nutrients[i - j]));
            }
            right[i] = maxRight;
        }

        for (int i = 0; i <= x; ++i) {
            int maxCombined = 0;
            for (int j = 0; j <= i; ++j) {
                maxCombined = max(maxCombined, left[j] + right[i - j]);
            }
            node->nutrients[i] = maxCombined;
        }
    }
}

int main() {
    string line;
    getline(cin, line); // Read the tree representation
    int x;
    cin >> x;

    Node* root = createNode(line, x);
    solve(root, x);
    cout << root->nutrients[x] << endl;

    return 0;
}