def solve(a,b):
    i=0
    for j in range(len(b)):
        if (j) and ( i<(len(a)-1) ) and a[i+1]==b[j]:
            i+=1
        elif a[i]!=b[j]:
            return False
    return i == len(a)-1

n = int(input())
for _ in range(n):
    s = input()
    t = input()
    print('YES' if solve(s,t)else 'NO')


# from itertools import groupby
#
# n = int(input())
# for _  in range(n):
#     str1 = input()
#     str2 = input()
#
#     li1 = [''.join(k) for _,k in groupby(str1)]
#     li2 = [''.join(k) for _,k in groupby(str2)]
#
#     if len(li1) != len(li2) or len(li2) < len(li1):
#         print('NO')
#         continue
#     for i,j in zip(li1, li2):
#         a = len(i)<len(j)
#         b = set(i) != set(j)
#         if len(i)>len(j) or set(i) != set(j):
#             print('NO')
#             break
#     else:
#         print('YES')
