#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> heights(n);
    for (int i = 0; i < n; ++i) {
        cin >> heights[i];
    }

    // dp[i][j] stores the most symmetric crop starting at i with a length of j
    vector<vector<int>> dp(n, vector<int>(n + 1, 0));
    vector<int> min_symmetrys(n + 1, INT_MAX); 
    min_symmetrys[0] = 0;
    min_symmetrys[1] = 0;

    // Initialize dp array for lengths 1 and 2
    for (int i = 0; i < n; ++i) {
        dp[i][1] = 0;
        if (i < n - 1) {
            dp[i][2] = abs(heights[i] - heights[i + 1]);
            min_symmetrys[2] = min(min_symmetrys[2], dp[i][2]);
        }
    }

    // Compute dp array for lengths 3 and above
    for (int j = 3; j <= n; ++j) {
        for (int i = 0; i <= n - j; ++i) {
            dp[i][j] = dp[i + 1][j - 2] + abs(heights[i] - heights[i + j - 1]);
            min_symmetrys[j] = min(min_symmetrys[j], dp[i][j]);
        }
    }

    // Output the minimum symmetries for each length
    for (int i = 1; i < min_symmetrys.size(); ++i) {
        cout << min_symmetrys[i] << ' ';
    }
    cout << endl;

    return 0;
}
