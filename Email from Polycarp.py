from itertools import groupby

n = int(input())
for _  in range(n):
    str1 = input()
    str2 = input()

    li1 = [''.join(k) for _,k in groupby(str1)]
    li2 = [''.join(k) for _,k in groupby(str2)]

    if len(li1) != len(li2) or len(li2) < len(li1):
        print('NO')
        continue
    for i,j in zip(li1, li2):
        a = len(i)<len(j)
        b = set(i) != set(j)
        if len(i)>len(j) or set(i) != set(j):
            print('NO')
            break
    else:
        print('YES')