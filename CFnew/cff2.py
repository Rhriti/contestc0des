for _ in range(int(input())):
    n,k=map(int,input().split())
    # def count_ways(n, k):
    #     ways = (1 << k) - 1
    #     return min(ways, n)


    # result = count_ways(n, k)
    # print(result+1)
    def count_ways(n, k):
        ways = min((1 << k) - 1, n)
        return ways


    result = count_ways(n, k)
    print(result+1)

