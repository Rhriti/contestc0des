#include <iostream>
#include <vector>
#include <deque>
#include <unordered_set>
#include <map>

using namespace std;

int main() {
    int row, col;
    cin >> row >> col;

    vector<vector<char>> g(row, vector<char>(col));
    pair<int, int> start, end;
    
    for (int r = 0; r < row; ++r) {
        string s;
        cin >> s;
        for (int c = 0; c < col; ++c) {
            g[r][c] = s[c];
            if (s[c] == 'A') {
                start = make_pair(r, c);
            } else if (s[c] == 'B') {
                end = make_pair(r, c);
            }
        }
    }

    deque<pair<int, int>> st;
    unordered_set<pair<int, int>> v;
    map<pair<int, int>, pair<int, int>> par;
    bool f = false;

    st.push_back(start);
    v.insert(start);
    par[start] = start;

    while (!st.empty()) {
        deque<pair<int, int>> t;
        while (!st.empty()) {
            pair<int, int> out = st.back();
            st.pop_back();
            int r = out.first;
            int c = out.second;

            if (make_pair(r, c) == end) {
                f = true;
                break;
            }

            int dr[4] = {1, -1, 0, 0};
            int dc[4] = {0, 0, 1, -1};

            for (int i = 0; i < 4; ++i) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (nr >= 0 && nr < row && nc >= 0 && nc < col && v.find(make_pair(nr, nc)) == v.end() &&
                    (g[nr][nc] == '.' || g[nr][nc] == 'B')) {
                    v.insert(make_pair(nr, nc));
                    t.push_back(make_pair(nr, nc));
                    par[make_pair(nr, nc)] = make_pair(r, c);
                }
            }
        }

        st = t;

        if (f) {
            break;
        }
    }

    if (!f) {
        cout << "NO" << endl;
    } else {
        deque<char> order;
        pair<int, int> itr = end;

        while (par[itr] != itr) {
            if (par[itr].first > itr.first) {
                order.push_front('U');
            } else if (par[itr].first < itr.first) {
                order.push_front('D');
            } else if (par[itr].second > itr.second) {
                order.push_front('L');
            } else {
                order.push_front('R');
            }

            itr = par[itr];
        }

        cout << "YES" << endl;
        cout << order.size() << endl;

        for (char ele : order) {
            cout << ele;
        }
        cout << endl;
    }

    return 0;
}
