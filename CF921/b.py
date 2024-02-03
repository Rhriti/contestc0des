def find_factors(number):
    factors = []
    i = 1
    while i * i <= number:
        if number % i == 0:
            factors.append(i)
            # If the factors are distinct, add the other factor
            if i != number // i:
                factors.append(number // i)
        i += 1
    return factors


for _ in range(int(input())):
    x,n=map(int,input().split())
    fac=find_factors(x)
    final=1
    for ele in fac:
        if x//ele>=n:final=max(final,ele)
         
    print(final)
    
