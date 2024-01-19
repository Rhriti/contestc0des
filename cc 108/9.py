
for _ in range(int(input())):
    n=int(input())
    s=input()
    memo={}

    def f(index,rem):
        #base case
        if (index,rem) in memo:return memo[(index,rem)]
        if index==n:
            if rem!=0:return 0
            else:return 1
        
        if s[index]!='?':
            if rem>=int(s[index]):
                memo[(index,rem)]=f(index+1,rem-int(s[index]))
                return memo[(index,rem)]
            else:
                memo[(index,rem)] =f(index+1,9+rem-int(s[index]))
                return memo[(index,rem)]
        else:
            c=0
            if index!=0:
                for j in range(10):
                    if rem>=j:
                        c+=f(index+1,rem-j)
                    else:
                        c+=f(index+1,9+rem-j)
            else:
                for j in range(1,10):
                    if rem>=j:
                        c+=f(index+1,rem-j)
                    else:
                        c+=f(index+1,9+rem-j)
            memo[(index,rem)]=c
 
            return c
 
    print(f(0,0))
                

            
        
