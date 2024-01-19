#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        vector<int> arr(n);

        for (int i = 0; i < n; i++) {
            cin >> arr[i];
            if (i % 2 == 0) {
                arr[i] = -arr[i];
            }
        }

        int s = 0;
        unordered_map<int, bool> pres;
        bool f = false;

        for (int i = 0; i < n; i++) {
            s += arr[i];
            if (pres.find(s) != pres.end()) {
                f = true;
                break;
            } else {
                pres[s] = true;
            }
        }

        if (f) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }

    return 0;
}
