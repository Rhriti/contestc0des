from collections import defaultdict
from math import comb
n=int(input())
arr=list(input().split())
even=[]
odd=[]
for ele in arr:
    if len(ele)%2==0:even.append(int(ele))
    else:odd.append(int(ele))
pres=[]
sums=[]
for ele in arr:
    s=0
    t=[]
    for ch in ele:
        s+=int(ch)
        t.append(s)
    sums.append(s)
    pres.append(t)

one=defaultdict(int)
two=defaultdict(int)
three=defaultdict(int)
four=defaultdict(int)
five=defaultdict(int)
print('pres',len(pres))
print('sums',len(sums))
for i in range(len(pres)):
    try:
        one[sums[i]-2*pres[i][  (len(pres[i])-1) //2 -1]]+=1
    except:pass
    try:
        two[sums[i]-2*pres[i][(len(pres[i])-2)//2-1]]+=1
    except:pass
    try:
        three[sums[i]-2*pres[i][  (len(pres[i])-3)//2-1     ]]+=1
    except:pass
    try:
        four[sums[i]-2*pres[i][   (len(pres[i])-4)//2-1   ]]+=1
    except:pass
    try:
        five[sums[i]-2*pres[i][  (len(pres[i])-5)//2-1   ]]+=1
    except:pass
final=0
print(one,two,three,four,five)
for ele in arr:
    l=len(ele)
    final+=comb(one[l],2)+comb(two[l],2)+comb(three[l],2)+comb(four[l],2)+comb(five[l],2)
print('ans',final)



