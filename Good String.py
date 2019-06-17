n = int(input())
s = input()
a = [s[0]]
for i in s[1:]:
    if a[-1] != i or len(a) % 2 == 0:
        a.append(i)
if len(a) % 2 == 1:
    a.pop()
print(n - len(a))
print(*a, sep='')

# good
# good
