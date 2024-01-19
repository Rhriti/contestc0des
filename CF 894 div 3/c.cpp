#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;
    
    for (int _ = 0; _ < t; ++_) {
        int n;
        cin >> n;
        
        vector<int> arr(n);
        for (int i = 0; i < n; ++i) {
            cin >> arr[i];
        }
        
        vector<int> newarr(arr[0], 0);
        for (int ele : arr) {
            newarr[ele - 1]++;
        }
        
        int s = 0;
        bool f = false;
        
        if (arr.size() == static_cast<size_t>(arr[0])) {
            for (int i = newarr.size() - 1; i >= 0; --i) {
                s += newarr[i];
                if (arr[i] != s) {
                    f = true;
                    break;
                }
            }
            if (f) {
                cout << "NO" << endl;
            } else {
                cout << "YES" << endl;
            }
        } else {
            cout << "NO" << endl;
        }
    }
    
    return 0;
}
