f=[0 for  _ in range(30)]
powers=[]
for i in range(30):powers.append(pow(2,i))
# print(powers)
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a==1:f[b]+=1
    else:
        fl=False
        w=b 
        for i in range(len(f)-1,-1,-1):
            if w==f[i]*powers[i]:
                fl=True
                print('YES')
                break
            elif w>f[i]*powers[i]:
                w-=f[i]*powers[i]
            else:
                if w%powers[i]==0:
                    fl=True
                    print('YES')
                    break
                else:
                    w=w%powers[i]
        if not fl:
            print('NO')
                

