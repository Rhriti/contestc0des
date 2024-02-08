#include <iostream>
#include <vector>

int main() {
    int t;
    std::cin >> t;

    while (t--) {
        int n;
        std::cin >> n;

        std::vector<int> s(n);
        for (int i = 0; i < n; ++i) {
            std::cin >> s[i];
        }

        std::vector<std::pair<int, char>> arr(26, {0, 'a'});
        std::string finalResult = "";

        for (int ele : s) {
            for (auto& ch : arr) {
                if (ch.first == ele) {
                    finalResult += ch.second;
                    ch.first += 1;
                    break;
                }
            }
        }

        std::cout << finalResult << std::endl;
    }

    return 0;
}
