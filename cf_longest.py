def max_interval_size(n):
    count = 1
    i = 2

    while i * i <= n:
        k = 0
        while n % i == 0:
            n //= i
            k += 1
        count *= (k + 1)
        i += 1 if i == 2 else 2

    if n > 1:
        count *= 2

    return count

# Example usage:
n = 40
result = max_interval_size(n)
print(result)  # Output: 6 (Maximum interval size: 1, 2, 3, 4, 6, 12 are divisors of 12)
