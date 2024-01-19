def isPerfectSquare(n):
    if n <= 1:
        return True
    
    left, right = 1, n

    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid
        
        if square == n:
            return True
        elif square < n:
            left = mid + 1
        else:
            right = mid - 1

    return False


for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    s=sum(arr)
    if isPerfectSquare(s):print('YES')
    else:print('NO')
