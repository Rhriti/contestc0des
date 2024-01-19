def distinctStrings(s):
    n=len(s)
    c=2**n
    for i in range(len(s)-1):
        c-=2**i+2**(n-i-2)
    return c

print(distinctStrings