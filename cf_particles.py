# for _ in range(int(input())):
#     n=int(input())
#     s=list(map(int,input().split()))
#     for i in range(n):
#         if s[i]>=0:
#             break
#     for j in range(n-1,-1,-1):
#         if s[j]>=0:
#             break
#     if j<i:
#         print(max(s))
#     elif j==i:
#         print(s[i])
#     else:
#         c1=c2=0
#         for t in range(i,j+1,2):
#             c1+=s[t]
#         for t in range(i+1,j+1,2):
#             c2+=s[t]
#         print(max(c1,c2))

def maximum_charge(particles):
    max_charge = float('-inf')
    particles.sort()

    while len(particles) > 1:
        c = particles.pop(0)
        if not particles:
            break

        left_charge = particles[0] if particles else 0
        right_charge = particles[-1] if particles else 0

        combined_charge = left_charge + right_charge
        particles[-1] = combined_charge
        max_charge = max(max_charge, combined_charge)

    return max_charge

print(maximum_charge([-3,1,4,-1,5,-9]))