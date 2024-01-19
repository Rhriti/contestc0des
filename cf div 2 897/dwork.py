from sys import stdin

input_fn = lambda: stdin.readline().rstrip('\r\n')

for _ in range(int(input_fn())):
    n, k = map(int, input_fn().split())
    a = [x - 1 for x in map(int, input_fn().split())]

    if k == 1:
        if a != list(range(n)):
            print('NO')
        else:
            print('YES')
        continue

    visited = [0] * n
    colors = [0] * n
    color_count = 1

    for i in range(n):
        if visited[i]:
            continue
        j, t = i, 1
        while not visited[i]:
            visited[i] = t
            colors[i] = color_count
            i, j = a[i], i
            t += 1
        color_count += 1
        if colors[i] == colors[j] and visited[j] - visited[i] + 1 != k:
            print('NO')
            break

    else:
        print('YES')
