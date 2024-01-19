#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3


def catchThieves(arr, n, k): 
    pol=set()
    thf=set()
    c=0
    try:
        index=arr.index('P')
    except:
        return 0
    tl=cc=index+k
    for i in range(index+1,len(arr)):
        if i<=cc:
            if arr[i]=='T':
                tl=i
            else:
                if tl!=index:
                    pol.add(index)
                    thf.add(tl)
                    c+=1
                index=i
                cc=i+k
        else:
            if tl!=index:
                pol.add(index)
                thf.add(tl)
                c+=1
                
        
            if arr[i]=='P':
                index=i
                cc=index+k
    if tl!=index:
        pol.add(index)
        thf.add(tl)
        c+=1
       
    arr=arr[::-1]
    f=False
    for i in range(len(arr)):
        if arr[i]=='P'and arr[i] in pol:
            f=True
            index=i
            tl=cc=index+k
            break
    if not f:
        return c
    
    for i in range(index+1,len(arr)):
        if i<=cc:
            if arr[i]=='T'and i not in thf:
                tl=i
            if arr[i]=='P' and i not in pol:
                if tl!=index:
                    c+=1
                    index=i
                    cc=i+k
        else:
            if arr[i]=='P' and i not in pol:
                index=i
                cc=index+k
    return c
                    
print(catchThieves(['P','T','T','P','T'],5,1)) 
print('upar')