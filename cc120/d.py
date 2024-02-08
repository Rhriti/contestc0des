# Python3 code to compute
# sum of subarray elements

# function compute sum
def count_subarrays_with_sum(permutation):
    N = len(permutation)
    prefix_sum = [0] * (N )
    count_sums = [0] * (N )
    result = 0

    for j in range(N):
        prefix_sum[j + 1] = prefix_sum[j] + permutation[j]

    count_sums[0] = 1  # Initialize with 0 to handle subarrays starting from index 0

    for j in range(1, N + 1):
        current_sum = prefix_sum[j]
        required_sum = current_sum - j

        if required_sum >= 0:
            result += count_sums[required_sum]

        count_sums[current_sum] += 1

    return result

# Example usage:
permutation = [1, 2, 3]
result = count_subarrays_with_sum(permutation)
print(result)
