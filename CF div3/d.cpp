#include <iostream>
#include <cmath>

int LCM(int a, int b) {
    int greater = std::max(a, b);
    int smallest = std::min(a, b);
    for (int i = greater; i <= a * b; i += greater) {
        if (i % smallest == 0) {
            return i;
        }
    }
    return -1; // Return -1 to indicate no LCM found (optional).
}

int main() {
    int test_cases;
    std::cin >> test_cases;
    
    for (int _ = 0; _ < test_cases; ++_) {
        int n, x, y;
        std::cin >> n >> x >> y;
        
        int xarr = std::floor(n / x);
        int yarr = std::floor(n / y);
        
        int common = std::floor(n / LCM(x, y));
        xarr -= common;
        yarr -= common;
        
        int sumy = (yarr * (yarr + 1)) / 2;
        int sumx = (xarr / 2) * (2 * n - xarr + 1);
        
        std::cout << sumx - sumy << std::endl;
    }
    
    return 0;
}
