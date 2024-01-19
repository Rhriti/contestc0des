#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

unordered_map<int, vector<int>> g;
unordered_map<int, int> val;
unordered_map<int, int> f;
unordered_map<int, int> c;

int dfs(int node) {
    c[val[node]]++;
    f[node] = c.size();

    for (int ch : g[node])
        dfs(ch);

    c[val[node]]--;
    if (c[val[node]] == 0)
        c.erase(val[node]);

    return f[node];
}

int dfs1(int node) {
    if (g[node].size() == 2) {
        int left = dfs1(g[node][0]);
        int right = dfs1(g[node][1]);
        int maxm = max((left - f[node] + 1) * (right - f[node] + 1), 1);
        return max({ left, right, f[node] });
    } else if (g[node].size() == 1) {
        int left = dfs1(g[node][0]);
        return max(left, f[node]);
    } else if (g[node].size() == 0) {
        return f[node];
    } else {
        int one = dfs1(g[node][0]);
        int two = dfs1(g[node][1]);
        for (int i = 2; i < g[node].size(); ++i) {
            int ch = g[node][i];
            if (two < dfs1(ch) && dfs1(ch) < one)
                two = dfs1(ch);
            if (dfs1(ch) >= one) {
                int t = one;
                one = dfs1(ch);
                two = t;
            }
        }
        return max((one - f[node] + 1) * (two - f[node] + 1), 1);
    }
}

int main() {
    int T;
    cin >> T;

    while (T--) {
        int n;
        cin >> n;
        g.clear();
        val.clear();
        f.clear();
        c.clear();

        vector<int> par(n);
        for (int i = 1; i < n; ++i) {
            int parent;
            cin >> parent;
            par[i] = parent;
            g[parent].push_back(i + 1);
        }

        for (int i = 1; i <= n; ++i) {
            int v;
            cin >> v;
            val[i] = v;
        }

        dfs(1);
        cout << dfs1(1) << endl;
    }

    return 0;
}
d.