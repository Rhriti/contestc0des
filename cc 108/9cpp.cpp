#include <iostream>
#include <unordered_map>
#include <string>

int countOutcomes(std::string s) {
    int n = s.length();
    std::unordered_map<std::pair<int, int>, int> memo;

    int f(int index, int rem) {
        // Base case
        if (memo.count({index, rem}) > 0) {
            return memo[{index, rem}];
        }
        if (index == n) {
            if (rem != 0) {
                return 0;
            } else {
                return 1;
            }
        }

        // Handling non-wildcard characters
        if (s[index] != '?') {
            if (rem >= int(s[index])) {
                memo[{index, rem}] = f(index + 1, rem - int(s[index]));
                return memo[{index, rem}];
            } else {
                memo[{index, rem}] = f(index + 1, 9 + rem - int(s[index]));
                return memo[{index, rem}];
            }
        }

        // Handling wildcard characters
        else {
            int c = 0;
            for (int j = 0; j < 10; ++j) {
                if (rem >= j) {
                    c += f(index + 1, rem - j);
                } else {
                    c += f(index + 1, 9 + rem - j);
                }
            }
            memo[{index, rem}] = c;
            return c;
        }
    }

    return f(0, 0);
}

int main() {
    std::string s = "??1??3";
    int count = countOutcomes(s);
    std::cout << count << std::endl;
    return 0;
}
