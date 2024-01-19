for _ in range(int(input())):
    n=int(input())
    s=input()[::-1]
    zeros=sum(1 for ele in s if ele=='0')
    zero_arr=[i for i in range(zeros)]
    j=0
    for i in range(len(s)):
        if s[i]=='0':
            zero_arr[j]=i-j
            j+=1
    sums=0
    pres=[]
    for ele in zero_arr:sums+=ele;pres.append(sums)
    final=[]

    for i in range(1,n+1):
        if i<=len(zero_arr):final.append(pres[i-1]) 
        else:final.append(-1)
    print(*final)