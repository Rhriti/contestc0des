T = 0 # Total possibilities
H = {} # counts all possible (A[k])%D = Key from index k
A=[3,3,4,7,8]
D=5

for k in range(2, len(A)):
  key = A[k]%D
  H[key] = H.get(key,0) + 1

for j in range(1, len(A)):
  if j >= 2:
    H[A[j]%D] -= 1 # when j increments it reduces options for A[k]
  for i in range(j):
    matching_val = (D - (A[i]+A[j]) % D ) % D
    to_add = H.get(matching_val, 0)
    T += to_add

return T

def getTripletCount(arr,d):
    T = 0 # Total possibilities
    H = {} # counts all possible (A[k])%D = Key from index k
    A=arr
    D=d

    for k in range(2, len(A)):
    key = A[k]%D
    H[key] = H.get(key,0) + 1

    for j in range(1, len(A)):
    if j >= 2:
        H[A[j]%D] -= 1 # when j increments it reduces options for A[k]
    for i in range(j):
        matching_val = (D - (A[i]+A[j]) % D ) % D
        to_add = H.get(matching_val, 0)
        T += to_add

    return T

print(getTripletCount([]))