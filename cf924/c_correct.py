

def f(n, x, t):
    res = [n]
    ret = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append(i)
    for r in res:
        a, b = r, n // r
        if a % 2 == 0 and 2*x - 2 < a < 2*t - 2:
            ret.add(a)
        if b % 2 == 0 and 2*x - 2 < b < 2*t - 2:
            ret.add(b)
    return ret


def solve():
    # n = int(input().strip())
    n, x = [int(i) for i in input().strip().split(' ')]
    n -= 1
    x -= 1
    ans = f(n - x, x, n + 1) | f(n + x, x, n + 1)
    print(ans)
    print(len(ans))


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        solve()
