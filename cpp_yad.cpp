#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

void dfs(int node, int c, unordered_map<int, vector<pair<int, int>>>& g, unordered_map<int, int>& dis, unordered_set<int>& v) {
    v.insert(node);
    dis[node] = c;
    for (auto& ch : g[node]) {
        if (v.find(ch.first) == v.end()) {
            dfs(ch.first, c + ch.second, g, dis, v);
        }
    }
}

void countCompatiblePairs(int nodes, vector<int>& frm, vector<int>& to, vector<int>& wei, vector<int>& val) {
    unordered_map<int, vector<pair<int, int>>> g;
    unordered_map<int, pair<int, int>> par;
    for (int i = 0; i < frm.size(); ++i) {
        g[frm[i]].push_back({to[i], wei[i]});
        par[to[i]] = {frm[i], wei[i]};
    }

    unordered_map<int, int> dis;
    unordered_set<int> v;
    dfs(1, 0, g, dis, v);

    int final = 0;
    for (int node = 1; node <= nodes; ++node) {
        int value = val[node - 1];
        int distance = 0;
        while (true) {
            distance += par[node].second;
            node = par[node].first;
            if (distance <= value) {
                final += 1;
            } else {
                break;
            }
            if (node == 1) break;
        }
    }
    cout << final - 1 << endl;
}