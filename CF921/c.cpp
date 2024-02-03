#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <string>

using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, k, m;
        cin >> n >> k >> m;
        string s;
        cin >> s;

        int need = n - 1;
        unordered_map<char, int> g;

        for (char ele = 'a'; ele < 'a' + k; ele++) {
            g[ele] = 0;
        }

        for (char ele : s) {
            if (g.find(ele) != g.end()) {
                g[ele]++;
            }
        }

        unordered_set<char> sets;
        for (char ele = 'a'; ele < 'a' + k; ele++) {
            sets.insert(ele);
        }

        bool f = true;
        string final = "";

        for (char ele : s) {
            if (g.find(ele) != g.end()) {
                g[ele]--;
            }

            if (sets.find(ele) != sets.end()) {
                for (const auto& entry : g) {
                    char k = entry.first;
                    int v = entry.second;
                    if (v < need) {
                        f = false;
                        final = ele + string(need, k);
                        break;
                    }
                }
                if (!f) {
                    break;
                }
                sets.erase(ele);
            }
        }

        if (!f) {
            cout << "NO" << endl;
            cout << final << endl;
        } else {
            if (sets.empty()) {
                cout << "YES" << endl;
            } else {
                cout << "NO" << endl;
                cout << final << endl;
            }
        }
    }

    return 0;
}
