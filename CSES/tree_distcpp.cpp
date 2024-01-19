#include <iostream>
#include <vector>
#include <unordered_map>

std::unordered_map<int, std::vector<int>> g, tree;
std::unordered_map<int, int> par, height, uphei;

void dfs(int node) {
    tree[node];
    for (int ch : g[node]) {
        if (tree.find(ch) == tree.end()) {
            tree[node].push_back(ch);
            par[ch] = node;
            dfs(ch);
        }
    }
}

int dfs_height(int node) {
    if (height.find(node) != height.end()) {
        return height[node];
    }
    height[node] = 0;
    for (int ch : tree[node]) {
        if (height.find(ch) == height.end()) {
            height[node] = std::max(height[node], 1 + dfs_height(ch));
        }
    }
    return height[node];
}

int dfs_uphei(int node) {
    if (uphei.find(node) != uphei.end()) {
        return uphei[node];
    }
    uphei[node] = dfs_uphei(par[node]) + 1;
    for (int ch : tree[par[node]]) {
        if (ch != node) {
            uphei[node] = std::max(uphei[node], height[ch] + 2);
        }
    }
    return uphei[node];
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    
    int n;
    std::cin >> n;
    
    for (int i = 0; i < n - 1; ++i) {
        int a, b;
        std::cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }
    
    dfs(1);
    par[1] = 1;
    dfs_height(1);
    
    for (int i = 1; i <= n; ++i) {
        if (uphei.find(i) == uphei.end()) {
            dfs_uphei(i);
        }
    }
    
    for (int i = 1; i <= n; ++i) {
        std::cout << std::max(uphei[i], height[i]) << ' ';
    }
    std::cout << '\n';
    
    return 0;
}
