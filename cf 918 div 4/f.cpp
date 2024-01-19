#include <iostream>
#include <vector>
#include <set>

int main() {
    int t;
    std::cin >> t;

    while (t--) {
        int n;
        std::cin >> n;
        std::vector<std::pair<int, int>> arr(n);

        for (int i = 0; i < n; ++i) {
            std::cin >> arr[i].first >> arr[i].second;
        }

        std::sort(arr.begin(), arr.end());

        std::set<int> endpoint_set;
        int final = 0;

        for (const auto& segment : arr) {
            final += endpoint_set.size() - std::distance(endpoint_set.begin(), endpoint_set.lower_bound(segment.second));
            endpoint_set.insert(segment.second);
        }

        std::cout << final << std::endl;
    }

    return 0;
}
