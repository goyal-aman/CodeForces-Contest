import sys
from math import *
n = int(input())
org = [0]*n
f = [0]*n
c = [0]*n
sum_f = 0
for i in range(n):
    num = float(sys.stdin.readline().rstrip())
    org[i] = num
    f[i] = floor(num)
    sum_f += f[i]
    c[i] = ceil(num)

i = 0
while sum_f<0 and i<n:
    if f[i]<c[i]:
        sum_f+=1
        f[i]=c[i]
    i+=1
#edge case: In any case we cannot get sum_f =0
if i>n:
    print(-1)
    exit()

    i+=1
for i in f:
    print(i)













