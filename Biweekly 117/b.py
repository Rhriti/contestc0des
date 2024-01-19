def nCr(n, r):
    # Calculate binomial coefficient C(n, r)
    res = 1
    for i in range(r):
        res *= (n - i)
        res //= (i + 1)
    return res

def distribute_candies(n, limit):
    # Calculate C(n+2, 2) using the nCr function
    result = nCr(n + 2, 2)

    # Subtract the cases where one child gets more than the limit
    for i in range(1, min(n, limit) + 1):
        # Calculate C(n-i+1, 2) * C(i+1, 1) * C(i+n-1, n-1)
        result -= nCr(n - i + 1, 2) * nCr(i + 1, 1) * nCr(i + n - 1, n - 1)

    return result

# Example usage:
n = 5
limit = 2
result = distribute_candies(n, limit)
print(result)
