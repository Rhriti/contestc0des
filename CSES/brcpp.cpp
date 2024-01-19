#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

unordered_map<int, vector<int>> g;

void dfs(int node, unordered_map<int>& v) {
    v.insert(node);
    for (int ch : g[node]) {
        if (v.find(ch) == v.end()) {
            dfs(ch, v);
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }

    unordered_map<int> v;
    int count = 0;
    vector<int> order;

    for (int i = 1; i <= n; ++i) {
        if (v.find(i) == v.end()) {
            count++;
            order.push_back(i);
            dfs(i, v);
        }
    }

    cout << count - 1 << endl;
    for (int i = 0; i < order.size() - 1; ++i) {
        cout << order[i] << " " << order[i + 1] << endl;
    }

    return 0;
}
