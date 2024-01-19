def hcf(x,y):
    if x==y:
        return x
    return hcf(abs(x-y),min(x,y))

print(hcf(12,30))

def gcd(x,y):
    if y==0:
        return x
    return gcd(y,x%y)
print(gcd(3,12))


def lcm(x,y):
    return x*y//hcf(x,y)

print(lcm(5,6))