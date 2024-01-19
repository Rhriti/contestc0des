import sys, random
input = iter(sys.stdin.readlines()).__next__
RANDOM = random.randrange(2**62)

def hash_int(key):
    return key ^ RANDOM

def solve():
    N = int(input())
    ans = {}
    pref = [val if i % 2 == 0 else -val for i, val in enumerate(map(int, input().split()))]

    d = set([hash_int(0), hash_int(pref[0])])

    for i in range(1, N):
        pref[i] += pref[i-1]
        if hash_int(pref[i]) in d:
            print("YES")
            return
        d.add(hash_int(pref[i]))
    print("NO")

def main():
    TC = int(input())
    for _ in range(TC):
        solve()

main()