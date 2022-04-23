#include <bits/stdc++.h>
using namespace std;

int n;
vector<bool> visited;

class Node {    
  public:             
    vector<string> move;        
    int level;  
};

vector<string> split(string s, const char delimiter) {
    size_t start = 0;
    size_t end = s.find_first_of(delimiter);
    vector<string> output;
    while (end <= string::npos) {
	    output.emplace_back(s.substr(start, end - start));
	    if (end == string::npos)
	    	break;
    	start = end + 1;
    	end = s.find_first_of(delimiter, start);
    }
    return output;
}

bool done(vector<string> move) {
  int i = 0;
  while (i < n && move[i] == to_string(i + 1))
    i++;
  return i == n;
}

int moveBase(vector<string> move) {
  int baseN = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < move[i].length(); j++) {
      int x = move[i][j] - '0' - 1;
      baseN += i * pow(n, x);
    }
  }
  return baseN;
}

vector<string> createNewMove(vector<string> old, int n1, int n2) {
  vector<string> newMove;
  for (int i = 0; i < n; i++)
    newMove.push_back(old[i]);
  
  newMove[n2] = newMove[n1].substr(0, 1) + newMove[n2];
  if (newMove[n1].length() > 0)
    newMove[n1] = newMove[n1].substr(1);

  if (n2 < n1 && newMove[n2].substr(0, 1) == to_string(n))
    return old;
  else
    return newMove;
}

int search(vector<string> move) {
  if (done(move))
    return 0;
  else {
    vector<Node> tree;
    Node init;
    init.move = move;
    init.level = 0;
    tree.push_back(init);
    while (tree.size() > 0) {
      Node x = tree[0];
      tree.erase(tree.begin());
      for (int i = 0; i < n; i++) {
        if (i < n - 1) {
          if (x.move[i + 1].length() == 0 || x.move[i][0] < x.move[i + 1][0]) {
            vector<string> newMove = createNewMove(x.move, i, i + 1);
            int baseN = moveBase(newMove);
            if (!visited[baseN]) {
              visited[baseN] = true;
              Node next;
              next.move = newMove;
              next.level = x.level + 1;
              tree.push_back(next);
              if (done(newMove)) {
                return x.level + 1;
              }
            }
          }
        }

        if (i > 0) {
          if (x.move[i - 1].length() == 0 || x.move[i][0] < x.move[i - 1][0]) {
            vector<string> newMove = createNewMove(x.move, i, i - 1);
            int baseN = moveBase(newMove);
            if (!visited[baseN]) {
              visited[baseN] = true;
              Node next;
              next.move = newMove;
              next.level = x.level + 1;
              tree.push_back(next);
              if (done(newMove)) {
                return x.level + 1;
              }
            }
          }
        }
      }
    }
    return -1;
  }
}

int main() {
  cin >> n;
  while (n > 0) {
    visited.clear();
    for (int i = 0; i < pow(n, n) + 1; i++) 
      visited.push_back(false);
    
    cin.ignore();
    string s;
    getline(cin, s);
    vector<string> move = split(s, ' ');

    int result = search(move);
    if (result >= 0) 
      cout << result << endl;
    else 
      cout << "IMPOSSIBLE" << endl;
    
    cin >> n;
  }
}
