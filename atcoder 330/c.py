def minimum_value(D):
    # Calculate the minimum value of |x^2 + y^2 - D|
    minimum_value = D

    # Try different values of x and y to find the minimum value
    for x in range(0, 100):
        for y in range(0, 100):
            if abs(x**2 + y**2 - D) < minimum_value:
                minimum_value = abs(x**2 + y**2 - D)

    return minimum_value

# Example usag
D = 264428617

minimum_value = minimum_value(D)
print("Minimum value:", minimum_value)
