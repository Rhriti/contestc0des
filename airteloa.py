s=[10,4,-1,4]
def dp(index):
    if index>=len(s) or s[index]==-1:
        return []

    left=dp(2*index+1)
    right=dp(2*index+2)
    if len(left)>len(right):
        left.append('L')
        return left
    else:
        right.append('R')
        return right
ans=dp(0)
print(ans)