def min_operations_to_equalize(arr, m):
    max_element = max(arr)
    operations = 0
    
    for num in arr:
        diff = max_element - num
        operations += diff // m
    
    return operations

# Example usage:
arr = [1,1,2,2,4,8]
m = 3
min_ops = min_operations_to_equalize(arr, m)
print(f"Minimum operations required: {min_ops}")
