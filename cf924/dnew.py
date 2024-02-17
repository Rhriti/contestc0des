# Function to find the length of the largest subarray
# having a sum at most k.
def atMostSum(arr, k):
	# Initialize the current sum to 0.
	sum_val = 0

	# Initialize a counter for the current subarray length
	# to 0.
	cnt = 0

	# Initialize the maximum subarray length to 0.
	maxcnt = 0

	for i in range(len(arr)):
		if arr[i] > k:

			# Reset the counter if an element is greater
			# than k.
			cnt = 0
			continue

		if (sum_val + arr[i]) <= k:

			# Include the current element in the subarray.
			# Increment the subarray length.
			cnt += 1
			sum_val += arr[i]
		else:
			cnt += 1
			sum_val += arr[i]

			# If the sum exceeds k, remove elements from
			# the subarray until the sum is less than or
			# equal to k.
			while sum_val > k:
				sum_val -= arr[i - cnt + 1]
				cnt -= 1

		# Update the maximum subarray length.
		maxcnt = max(cnt, maxcnt)

	return maxcnt

# Main function
if __name__ == "__main__":
	arr = [1, 2, 1, 0, 1, 1, 0]
	k = 4

	# Print the length of the longest
	# subarray with sum at most k.
	print(atMostSum(arr, k))
