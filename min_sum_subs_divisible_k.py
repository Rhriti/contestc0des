# def min_sum_subsequence(nums, current_sum, idx, k):
#     # Base case: if the sum is divisible by k, return the current sum
#     if current_sum % k == 0:
#         return current_sum

#     # Base case: if we have explored all elements, return a large value
#     if idx == len(nums):
#         return float('inf')

#     # Recursive case: explore two possibilities - include or exclude the current element
#     include_current = min_sum_subsequence(nums, current_sum + nums[idx], idx + 1, k)
#     exclude_current = min_sum_subsequence(nums, current_sum, idx + 1, k)

#     return min(include_current, exclude_current)

# # Example usage:
# arr = [1, 2, 3, 4, 5]
# k_value = 3
# result = min_sum_subsequence(arr, 0, 0, k_value)

# if result == float('inf'):
#     print("No subsequence with the given sum.")
# else:
#     print("Minimum sum subsequence divisible by", k_value, "is:", result)



def min_sum_subsequence(nums, k):
    n = len(nums)
    memo = {}

    def dp(i, current_sum):
        if (i, current_sum) in memo:
            return memo[(i, current_sum)]

        if current_sum % k == 0:
            memo[(i, current_sum)] = current_sum
            return current_sum

        if i == n:
            return float('inf')

        include_current = dp(i + 1, current_sum + nums[i])
        exclude_current = dp(i + 1, current_sum)

        result = min(include_current, exclude_current)
        memo[(i, current_sum)] = result

        return result

    result = dp(0, 0)
    return result if result != float('inf') else -1

# Example usage:
arr = [1, 2, 3, 4, 5]
k_value = 3
result = min_sum_subsequence(arr, k_value)

if result == -1:
    print("No subsequence with the given sum.")
else:
    print("Minimum sum subsequence divisible by", k_value, "is:", result)
