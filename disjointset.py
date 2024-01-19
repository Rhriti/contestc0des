#below is DS for disjoint set
size={}
parent={}
#parent ka memo bana do.that is pathcompression
# parent={}

def make(node):
    parent[node]=node
    size[node]=1 #is set me abhi ke lie 
    # parent[node]=node
     
def find(node):
    #memo lga idhar
    #or just parent kohi update krod ,no need of parent/memo
    if parent[node]==node:
        return node

    currroot=find(parent[node])
    parent[node]=currroot
    return currroot

def union(a,b):
    parenta=find(a)
    parentb=find(b)
    if parenta!=parentb:
        if size[parenta]>size[parentb]:
            #agar b wala tree/set chota haito usko add kro a ke parent se ,,taki tree ki size same rhe .
            parent[parentb]=parenta
            # parent[parentb]=parent[parenta]
            size[parenta]+=size[parentb]
            size[parentb]=size[parenta]
        else:
            size[parentb]+=size[parenta]
            size[parenta]=size[parentb]
            parent[parenta]=parentb
            # parent[parenta]=parent[parentb]
        
  
for i in range(1,7):
    make(i)
union(1,2)
print(parent[1],parent[2])
union(2,3)
print(parent[2],parent[3])
union(5,6)
print(parent[5],parent[6])
union(1,5)
print(parent[1],parent[5])
union(1,4)
print(parent[1],parent[4])
# print(parent)
# print(parent)
# print(size)