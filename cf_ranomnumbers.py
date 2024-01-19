#ranom numbers 
from collections import defaultdict
for _ in range(int(input())):
    s=input()
    d=[]
    for ele in s:
        if ele=='A':
            d.append(1)
        if ele=='B':
            d.append(10)
        if ele=='C':
            d.append(100)
        if ele=='D':
            d.append(1000)
        if ele=='E':
            d.append(10000)
    pp=[]
    maxm=float('-inf')
    for i in range(len(s)-1,-1,-1):
        if d[i]>maxm:
            maxm=d[i]
        pp.append(maxm)
    pp=list(reversed(pp))
    arr=[]
    count=0
    g=defaultdict(int)
    for i in range(len(s)-1):
        g[s[i]]+=1
        if pp[i+1]>d[i]:
            arr.append('not')
            count+=-d[i]
        else:
            arr.append('add')
            count+=d[i]
    arr.append('add')
    count+=d[-1]
    g[d[-1]]+=1
    if count==sum(d):
        #pahla a,b,c,d ko e ban do
        for ele in ['A','B','C','D']:
            if ele in g:
                count-=1
                count+=10000
                break
        print(count)
    else:
        snew=''
        for i in range(len(s)-1,-1,-1):
            if arr[i]=='not':
                snew+='E'
            else:
                snew+=s[i]
        snew=snew[::-1]
        s=snew
        d=[]
        for ele in s:
            if ele=='A':
                d.append(1)
            if ele=='B':
                d.append(10)
            if ele=='C':
                d.append(100)
            if ele=='D':
                d.append(1000)
            if ele=='E':
                d.append(10000)
        pp=[]
        maxm=float('-inf')
        for i in range(len(s)-1,-1,-1):
            if d[i]>maxm:
                maxm=d[i]
            pp.append(maxm)
        pp.reverse()
        arr=[]
        count=0
        g=defaultdict(int)
        for i in range(len(s)-1):
            g[s[i]]+=1
            if pp[i+1]>d[i]:
                arr.append('not')
                count+=-d[i]
            else:
                arr.append('add')
                count+=d[i]
        arr.append('add')
        count+=d[-1]
        print(count)





        