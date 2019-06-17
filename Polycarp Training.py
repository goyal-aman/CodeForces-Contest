n = int(input())
s = sorted(list(map(int, input().split())))
round = 0
for i in s:
    if i > round:
        round += 1
print(round)
