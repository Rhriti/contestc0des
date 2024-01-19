# cook your dish here
for _ in range(int(input())):
    l,n=map(int,input().split())
    if n<100:
        if n%8==0:
            print(n)
        else:
            nnew=str(n)
            prev=(n//8)*8
            prev=str(prev)
            nxt=(n//8)*8+8
            nxt=str(nxt)
            if len(prev)==len(nxt)==len(nnew):
                s1=0
                for i in range(l):
                    if nnew[i]==prev[i]:
                        s1+=1
                s2=0
                for i in range(l):
                    if nnew[i]==nxt[i]:
                        s2+=1
                if s1>s2 :
                    print(int(prev))
                else:
                    print(int(nxt))
            elif len(prev)!=len(nnew):
                print(int(nxt))
            else:
                print(int(prev))
    else:
        out=n%1000
        if out%8==0:
            print(n)
        else:
            nnew=str(out)
            prev=(out//8)*8
            prev=str(prev)
            nxt=(out//8)*8+8
            nxt=str(nxt)
            s1=0
            if len(nnew)==len(prev)==len(nxt):
                for i in range(len(nnew)):
                    if nnew[i]==prev[i]:
                        s1+=1
                s2=0
                for i in range(len(nnew)):
                    if nnew[i]==nxt[i]:
                        s2+=1
                if s1>s2 :
                    ans=n-out+int(prev)
                    print(ans)
                else:
                    ans=n-out+int(nxt)
                    print(ans)
            elif len(prev)==len(nnew):
                ans=n-out+int(prev)
                print(ans)
            else:
                print(n-out+int(nxt))
            
                    
                    
                    
                    
                    
                    
                    
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                