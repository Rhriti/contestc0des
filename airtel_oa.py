s=[0,1,2,3,4,5,6,7,9]
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def f(i,j):
    if i==j:
        return Node(s[i])
    if j-i==1:
        n=Node(s[i])
        n.right=Node(s[j])
        return n
    m=(i+j)//2
    l=f(i,m-1)
    r=f(m+1,j)
    n=Node(s[m])
    n.left=l
    n.right=r
    return n

root=f(0,len(s)-1)
arr=[]
def inorder(node):
    if node.left:
        inorder(node.left)
    arr.append(node.val)
    if node.right:
        inorder(node.right)
inorder(root)
print(arr)
