from collections import deque,Counter,defaultdict

def minWindow( s , t ):
    g=Counter(t)
    gnew=defaultdict(int)
    st=deque()
    j=i=0
    final=[0,float('inf')]
    allgnew=defaultdict(int)
    count=0
    
    while i<len(s):
        if count!=len(g):
            while i<len(s) and gnew!=g:
                if s[i] in g:
                    gnew[s[i]]+=1
                    if gnew[s[i]]==g[s[i]]:count+=1
                i+=1
        if count==len(g):
            
            while j<len(s) and count==len(g):
                if s[j] in gnew:gnew[s[j]]-=1
                if gnew[s[j]]<g[s[j]]:count-=1
                
                j+=1
            if i-j<final[1]-final[0]:final[0]=j;final[1]=i
            gnew[s[j]]-=1
            if gnew[s[j]]<=0:del gnew[s[j]]
            j+=1

    
    return s[final[0]:final[1]]
            
print(minWindow("ADOBECODEBANC","ABC"))