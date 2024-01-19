#include <iostream>
#include <vector>
#include <unordered_map>

int main() {
    int n, m;
    std::cin >> n >> m;
    
    std::unordered_map<int, std::vector<int>> g;
    for (int i = 0; i < m; i++) {
        int a, b;
        std::cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }
    
    std::unordered_map<int, int> assign;
    bool f = false;
    
    std::function<void(int, int)> dfs = [&](int node, int c) {
        assign[node] = c % 2;
        for (int ch : g[node]) {
            if (assign.count(ch)) {
                if (assign[node] + assign[ch] != 1) {
                    f = true;
                    break;
                }
            } else {
                dfs(ch, c + 1);
            }
        }
    };
    
    for (int ele = 1; ele <= n; ele++) {
        if (!assign.count(ele)) {
            dfs(ele, 0);
            if (f) {
                break;
            }
        }
    }
    
    if (f) {
        std::cout << "IMPOSSIBLE" << std::endl;
    } else {
        for (int ele = 1; ele <= n; ele++) {
            std::cout << assign[ele] + 1 << " ";
        }
        std::cout << std::endl;
    }
    
    return 0;
}
