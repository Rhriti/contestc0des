import sys
 
from math import gcd, floor, ceil, sqrt

import math
 
from bisect import bisect_left, bisect_right, insort

from collections import defaultdict, Counter, deque
 
from heapq import heappush, heappop, heapify

from string import ascii_lowercase, ascii_uppercase

from types import GeneratorType

from functools import reduce
 
input = sys.stdin.readline
 
# Read one line as int
def read_int():
    return int(input())
 
# Read one line and parse each word as an integer
def read_int_arr():
    return list(map(int,input().split()))
 
# Read n rows and parse each element as an integer
def read_int_matrix(n):
    return [list(map(int, input().split())) for _ in range(n)]
 
# Read one line and parse as string
def read_string():
    return input().strip()
 
# Read one line and parse each word as an string
def read_string_arr():
    return list(map(str,input().split()))
 
# Read n rows and parse each element as an string
# Can be used as a matrix
def read_string_list(n):
    return [input().strip() for _ in range(n)]

# n / 2 * (a + l), where a = 1 and l = n
def first_n(n):
    return n * (n + 1) // 2

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Sieve of eratosthenes
# <= n version
def primes_LTOE(n):
    if n <= 2:
        return []

    sieve = [True] * (n + 1)
    sieve[0], sieve[1] = False, False

    for i in range(2, int(n**0.5) + 1, 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return [i for i in range(n + 1) if sieve[i]]

# Unique prime factorisation
# Returns a set
def unique_prime_factors(x):
    res = set()
    if x % 2 == 0:
        res.add(2)
        while x % 2 == 0:
            x //= 2

    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            res.add(i)
            while x % i == 0:
                x //= i
        if x == 1:
            break

    if x > 2:
        res.add(x)

    return res

def prime_factors(n):
    res = []
    while n % 2 == 0:
        res.append(2)
        n = n // 2

    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            res.append(i)
            n = n // i

    if n > 2:
        res.append(n)

    return res


# Set of all factors
def all_fact(n):
    return set(
        reduce(
            list.__add__,
            ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0),
        )
    )

def binom_mod(n, r, m):
    if (r > n):
        return 0
         
    inv = [0 for i in range(r + 1)]
    inv[0] = 1
    if(r+1>=2):
        inv[1] = 1
 
    for i in range(2, r + 1):
        inv[i] = m - (m // i) * inv[m % i] % m
 
    ans = 1
 
    for i in range(2, r + 1):
        ans = ((ans % m) * (inv[i] % m)) % m
 
    for i in range(n, n - r, -1):
        ans = ((ans % m) * (i % m)) % m
         
    return ans

# Recursive depth hack, replace all 'return' with 'yield', and add 'yield' before all recursive calls
# end of func must also have yield, even if return none
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
 
    return wrappedfunc

MOD = 10**9 + 7
inf = float('inf')
ninf = float('-inf')
 
# (a+b-1) // b is the same as ceil(a/b) if b is positive, sometimes escapes precision rubbish

# ============================================ template ============================================ 
 
def solve():
    n,m = read_int_arr()
    g = defaultdict(dict)
    for i in range(m):
        u,v,w = read_int_arr()
        
        if v in g[u]:
            g[u][v] = min(g[u][v], w)
            g[v][u] = min(g[v][u], w)
        else:
            g[u][v] = w
            g[v][u] = w
    
    bikes = read_int_arr()
    seen = defaultdict(int)
    minh = [(0, bikes[0], 1)]

    while minh:
        cost, bike, node = heappop(minh)
        bike = min(bike, bikes[node - 1])

        if node == n:
            print(cost)
            return
        elif (bike, node) in seen and seen[(bike, node)] <= cost:
            continue
        seen[(bike, node)] = cost

        for v, w in g[node].items():
            heappush(minh, (cost + bike * w, bike, v))
    
    print(min(v for k, v in seen.items() if k[1] == n))
    
    
 
for case_num in range(int(input())):
    solve()
































from heapq import heappush, heappop

def solve():
    num_nodes, num_edges = map(int, input().split())
    adjacency_list = [[] for _ in range(num_nodes)]
    
    for _ in range(num_edges):
        node_a, node_b, weight = map(int, input().split())
        adjacency_list[node_a - 1].append([node_b - 1, weight])
        adjacency_list[node_b - 1].append([node_a - 1, weight])
    
    initial_weights = list(map(int, input().split()))
    heap = [[0, 0, initial_weights[0]]]
    visited_nodes = {}

    while heap:
        time, current_node, current_weight = heappop(heap)

        if current_node == num_nodes - 1:
            print(time)
            return

        if current_weight > initial_weights[current_node]:
            current_weight = initial_weights[current_node]

        if current_node in visited_nodes and visited_nodes[current_node] <= current_weight:
            continue
        else:
            visited_nodes[current_node] = current_weight

        for neighbor, edge_weight in adjacency_list[current_node]:
            heappush(heap, [time + edge_weight * current_weight, neighbor, current_weight])


for _ in range(int(input())):
    solve()
