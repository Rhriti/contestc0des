
def maxArrayValue(nums ) :
    s=nums
    while True:
        new=[]
        if len(s)%2==0:
            if len(s)>2:
                for i in range(0,len(s),2):
                    if s[i+1]>=s[i]:
                        new.append(s[i]+s[i+1])
                    else:
                        new.append(s[i])
                        new.append(s[i+1])
            else:
                if s[1]>=s[0]:
                    new=[s[1]+s[0]]
                else:
                    return max(s[0],s[1])
        else:
            for i in range(0,len(s)-1,2):
                if s[i+1]>=s[i]:
                    new.append(s[i]+s[i+1])
                else:
                    new.append(s[i])
                    new.append(s[i+1])
            new.append(s[-1])
        if len(new)==0 or s==new:
            return max(new)
        s=new

print(maxArrayValue([5,3,3]))