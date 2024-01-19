n, k, p = map(int, input().split())
prod = [0] * k
devplan = []
cost = []
sums = [0] * k

for _ in range(n):
    arr = list(map(int, input().split()))
    cost.append(arr[0])
    devplan.append(arr[1:])
    for i in range(k):
        sums[i] += arr[i + 1]

def dp(r, prod):
    # Base case
    if all(ele >= p for ele in prod):
        return 0
    if r == n:
        return float('inf')
    
    if (r, tuple(prod)) in memo:
        return memo[(r, tuple(prod))]

    mc = dp(r + 1, prod)  # Move to the next development plan
    for c in range(k):
        prod[c] += devplan[r][c]
    mc2 = cost[r] + dp(r + 1, prod)  # Choose the current development plan
    for c in range(k):
        prod[c] -= devplan[r][c]

    memo[(r, tuple(prod))] = min(mc, mc2)
    return memo[(r, tuple(prod))]

memo = {}  # Memoization dictionary
result = dp(0, prod)
if result == float('inf'):
    print(-1)
else:
    print(result)
