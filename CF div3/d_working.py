# from math import lcm
import sys
input = sys.stdin.readline
MOD = 10**9 + 7

def read_array(factory):
    return [factory(num) for num in input().strip().split()]
def print_array(arr):
    print(" ".join(map(str, arr)))

def gcd(x, y):
    if y == 0:
        return abs(x)
    return gcd(y, x%y)

def lcm(x, y):
    return x*y // gcd(x, y)

def solve(n, x, y):
    # We need to count the number of overlaps between
    # multiples of x <= n and multiples of y <= n
    mulx = n//x
    muly = n//y
    overlap = n//lcm(x, y)
    # The overlap numbers can be any numbers
    # mulx needs to be as high as possible
    # muly as low as possible
    mulx -= overlap
    muly -= overlap
    # print(mulx, muly)
    sumx = n*(n+1)//2 - ((n-mulx))*((n-mulx)+1)//2
    sumy = muly*(muly+1)//2
    print('sumy', sumy)
    print('sumx',sumx)
    return sumx-sumy

if __name__ == "__main__":
    # Read in input:
    t = int(input())

    # Call solution:
    for _ in range(t):
        n, x, y = read_array(int)
        try:
            ans = solve(n, x, y)
            print(ans)
        except Exception as e:
            print(e)

