def multiply(a,b,bound):
    val=a*b
    if val>bound:
        raise ValueError(f'multiplication of {a} and {b} with bound {bound} not posisble')
    else:
        return a*b

print(multiply)