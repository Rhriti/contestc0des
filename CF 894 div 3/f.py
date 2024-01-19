for _ in range(int(input())):
    w,f=map(int,input().split())
    w0=w
    f0=f
    n=int(input())
    arr=list(map(int,input().split()))
    c=1
    for ele in arr:
        if ele>=w and ele>=f:
            if w<f:
                w-=ele
            else:
                f-=ele
            c+=1
        elif ele>=w and ele<f:
            w-=ele
            c+=1
        elif ele>=f and ele<w:
            f-=ele
            c+=1
        else:
            #jo jyada bda hoga use bada kr de
            d1=ele-w
            times=d1//w0
            rem=d1%w0
            c1=c+times+1 if rem!=0 else times
            neww=w+w0*(times+1 if rem!=0 else times)
            newf=f+f0*(times+1 if rem!=0 else times)

            d2=ele-f
            times=d2//f0
            rem=d2%f0
            c2=c+times+1 if rem!=0 else times
            neww2=w+w0*(times+1 if rem!=0 else times)
            newf2=f+w0*(times+1 if rem!=0 else times)

            if max(neww,newf)>max(newf2,neww2):
                w=neww
                f=newf
                c=c1
                if ele>=w and ele>=f:
                    if w<f:
                        w-=ele
                    else:
                        f-=ele
                elif ele>=w and ele<f:
                    w-=ele
                else:
                    f-=ele
  
            else:
                w=neww2
                f=newf2
                c=c2
                if ele>=w and ele>=f:
                    if w<f:
                        w-=ele
                    else:
                        f-=ele
                elif ele>=w and ele<f:
                    w-=ele
                else:
                    f-=ele
        
        w+=w0
        f+=f0

    print('ans is ',c)

                