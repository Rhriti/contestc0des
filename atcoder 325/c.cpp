#include <iostream>
#include <vector>
#include <set>

using namespace std;

int row, col;
vector<string> g;
set<pair<int, int>> v;

void dfs(int i, int j) {
    v.insert({i, j});
    int dx[] = {1, -1, 0, 0, 1, -1, 1, -1};
    int dy[] = {0, 0, 1, -1, 1, -1, -1, 1};

    for (int k = 0; k < 8; k++) {
        int x = i + dx[k];
        int y = j + dy[k];
        if (x >= 0 && x < row && y >= 0 && y < col && v.find({x, y}) == v.end() && g[x][y] == '#') {
            dfs(x, y);
        }
    }
}

int main() {
    cin >> row >> col;
    g.resize(row);

    for (int i = 0; i < row; i++) {
        cin >> g[i];
    }

    int count = 0;
    for (int r = 0; r < row; r++) {
        for (int c = 0; c < col; c++) {
            if (v.find({r, c}) == v.end() && g[r][c] == '#') {
                count++;
                dfs(r, c);
            }
        }
    }

    cout << count << endl;

    return 0;
}
