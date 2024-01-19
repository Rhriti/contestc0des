#include <iostream>
#include <vector>
#include <set>

using namespace std;

int r, c;
vector<string> g;
set<pair<int, int>> v;

void dfs(int row, int col) {
    v.insert(make_pair(row, col));
    
    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, 1, 0, -1};
    
    for (int i = 0; i < 4; ++i) {
        int x = row + dx[i];
        int y = col + dy[i];
        
        if (x >= 0 && x < r && y >= 0 && y < c && v.find(make_pair(x, y)) == v.end() && g[x][y] == '.') {
            dfs(x, y);
        }
    }
}

int main() {
    cin >> r >> c;
    
    g.resize(r);
    for (int i = 0; i < r; ++i) {
        cin >> g[i];
    }
    
    int count = 0;
    for (int row = 0; row < r; ++row) {
        for (int col = 0; col < c; ++col) {
            if (g[row][col] == '.' && v.find(make_pair(row, col)) == v.end()) {
                count++;
                dfs(row, col);
            }
        }
    }
    
    cout << count << endl;
    
    return 0;
}
