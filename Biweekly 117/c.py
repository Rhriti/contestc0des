def count_good_strings(n):
    MOD = 10**9 + 7

    # Initialize a 2D DP array to store counts
    dp = [[[0] * 4 for _ in range(4)] for _ in range(n + 1)]

    # Base case: strings of length 1
    for i in range(4):
        for j in range(4):
            dp[1][i][j] = 1

    # Dynamic programming to count the number of good strings
    for length in range(2, n + 1):
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if i == j and j == k:
                        continue
                    dp[length][j][k] = (dp[length][j][k] + dp[length - 1][i][j]) % MOD

    # Sum up the counts for all combinations of the last two characters
    result = sum(dp[n][i][j] for i in range(4) for j in range(4)) % MOD
    return result

# Example usage:
n = 4
result = count_good_strings(n)
print(result)
