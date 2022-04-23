#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n, w, d;
    cin >> n >> w >> d;

    vector<int> walkways[n + 1];
    int dist[n + 1];
    for(int i = 1; i < n; i++)
        dist[i] = 1e9;
    dist[n] = 0;

    for(int i = 0; i < w; i++){
        int a, b;
        cin >> a >> b;
        walkways[b].push_back(a);
    }

    bool visited[n + 1];
    memset(visited, 0, sizeof(visited)); 
    visited[n] = true;

    queue<int> queue;
    queue.push(n);

    while (!queue.empty()) {
        int front = queue.front();
        queue.pop();

        for (int w: walkways[front]) {
            if (!visited[w]) {
                dist[w] = dist[front] + 1;
                visited[w] = true;
                queue.push(w);
            }
        }
    }

    int subway[n + 1];
    multiset<int> cumulative;

    for (int i = 1; i <= n; i++) {
        cin >> subway[i];
        cumulative.insert(i - 1 + dist[subway[i]]);
    }

    for (int i = 0; i < d; i++) {
        int first, second;
        cin >> first >> second;

        cumulative.erase(cumulative.find(first - 1 + dist[subway[first]]));
        cumulative.erase(cumulative.find(second - 1 + dist[subway[second]]));
        swap(subway[first], subway[second]);

        cumulative.insert(first - 1 + dist[subway[first]]);
        cumulative.insert(second - 1 + dist[subway[second]]);

        cout << *cumulative.begin() << endl;
    }
}