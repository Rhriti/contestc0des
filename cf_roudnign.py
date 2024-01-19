from collections import deque
for _ in range(int(input())):
    n=input()
    nums=[]
    for ele in n:
        nums.append(int(ele))
    index=None
    s=deque()
    s.append(nums[-1])
    i=len(nums)-2
    while i>=0:
        if nums[i]==9:
            if s[0]>=5:
                while i>=0 and nums[i]==9:
                    s.appendleft(nums[i])
                    i-=1
                continue
            else:
                s.appendleft(nums[i])
        else:
            if s[0]>=5:
                s.appendleft(nums[i]+1)
                index=i
            else:
                s.appendleft(nums[i])
        i-=1

    if s[0]>=5:
        snew='1'+'0'*len(s)
    else:
        if index is not None:
            snew=''
            for i in range(index+1):
                snew+=str(s[i])
            snew+='0'*(len(s)-1-index)

        else:
            snew=''
            for i in range(len(s)):
                snew+=str(s[i])

    print(snew)      
