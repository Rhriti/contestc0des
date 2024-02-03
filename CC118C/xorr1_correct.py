for _ in range(int(input())):
    x = int(input())
    a, b = 0, 0
    for i in range(30):
        if x & 2**i:
            a += b
            b = 2**i
    print(a, b)