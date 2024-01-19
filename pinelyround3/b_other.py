
t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    k = 1
    while True:
        arr = set([i % k for i in a])
        if len(arr) == 2:
            print(k)
            break
        else:
            k = 2 * k