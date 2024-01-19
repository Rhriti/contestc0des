#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

unordered_map<int, vector<int>> g;

int dfs(int node, int n) {
    if (node == n) {
        return 1;
    }
    int ways = 0;
    for (int ch : g[node]) {
        ways += dfs(ch, n);
    }
    return ways;
}

int main() {
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        g[a].push_back(b);
    }

    cout << dfs(1, n) << endl;

    return 0;
}
