import math
def binary_converter(binary,base=10):
    s=''
    for ele in binary:s+=str(ele)
    if base=='o':
        return oct(int(s,2))
    elif base=='h':
        return hex(int(s,2))
    elif base=='d':
        return int(s,2)
    else:
        return int(s)
    
print(binary_converter([1,0,1,0,1,1,1,0,1,0],'b'))