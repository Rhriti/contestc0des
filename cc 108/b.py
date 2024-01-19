def sieve_of_eratosthenes(n):
    primes = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    return primes

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_prime_palindromes(n):
    max_num = 10**n - 1
    primes = sieve_of_eratosthenes(max_num)
    even_digit_primes = []
    odd_digit_primes = []
    for i in range(2, max_num):
        if primes[i] and is_palindrome(i):
            if len(str(i)) % 2 == 0:
                even_digit_primes.append(i)
            else:
                odd_digit_primes.append(i)
    return even_digit_primes, odd_digit_primes

for _ in range(int(input())):
    n = int(input())
    even_digit_primes, odd_digit_primes = find_prime_palindromes(n)
    print("Odd digit prime palindromes:", odd_digit_primes)
    print("Even digit prime palindromes:", even_digit_primes)
    print('ans', len(even_digit_primes), len(odd_digit_primes))