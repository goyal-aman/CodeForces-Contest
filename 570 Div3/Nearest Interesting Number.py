def sum_digits(n):
    return sum(int(i) for i in str(n))

n = int(input())
if sum_digits((n))%4==0:
    print(n)
else:
    while sum_digits(int(n))%4!=0:
        n+=1
    print(n)