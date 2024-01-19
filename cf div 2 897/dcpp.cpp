#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

unordered_map<int, bool> memo;

bool dfs(vector<int>& arr, vector<int>& count, int node, int c, int k) {
    if (memo.find(node) != memo.end()) {
        return memo[node];
    }

    count[node] = c;
    int ch = arr[node];
    if (count[ch] == -1) {
        bool local = dfs(arr, count, ch, c + 1, k);
        memo[node] = local;
    } else {
        if (abs(count[node] - count[ch]) + 1 == k) {
            memo[node] = true;
        } else {
            memo[node] = false;
        }
    }

    return memo[node];
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;

        vector<int> arr(n);
        vector<int> count(n, -1);
        memo.clear();

        for (int i = 0; i < n; i++) {
            cin >> arr[i];
            arr[i]--;
        }

        string final = "YES";
        for (int i = 0; i < n; i++) {
            count.assign(n, -1);
            bool ans = dfs(arr, count, i, 0, k);
            if (!ans) {
                final = "NO";
                break;
            }
        }
        cout << final << endl;
    }

    return 0;
}
