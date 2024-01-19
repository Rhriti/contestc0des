# for _ in range(int(input())):
#     s1=input()
#     s2=input()
#     st=[]
#     f=False
#     for i in range(len(s1)):
#         if len(st)==0:
#             if s1[i]!=s2[i]:
#                 f=True
#                 break
#             else:
#                 st=[s1[i]]
#             continue

#         if s1[i]==s2[i]:
#             if len(st)>1:
#                 if s1[i]==st[0]:
#                     st=[]
#                 else:
#                     st.append(None)
#             else:
#                 st=[s1[i]]
#         else:
#             st.append(None)
#     if f:
#         print('NO')
#     else:
#         ans='YES'
#         for ele in st:
#             if ele is None:
#                 ans='NO'
#                 break
#         print(ans)