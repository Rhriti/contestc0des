def compare_exponents(n):
    # Assuming a, b, and c are equal for the sake of simplicity
    a = b = c = n // 3

    # Comparing n^n and a^a * b^b * c^c
    n_to_power_n = n ** n
    abc_to_power_abc = (a ** a) * (b ** b) * (c ** c)

    if n_to_power_n > abc_to_power_abc:
        return "n^n is greater than a^a * b^b * c^c"
    else:
        return "n^n is not greater than a^a * b^b * c^c"

# Example usage:
n = 4 # Replace with the desired value of n
result = compare_exponents(n)
print(result)
