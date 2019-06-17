n = int(input())
s = input()
x, y = n // 2, n // 2 + 1
while (x > 0 and s[x] == '0'):
    x -= 1
while (y < n and s[y] == '0'):
    y += 1
if x == 0:
    print(int(s[:y]) + int(s[y:]))
elif y == n:
    print(int(s[:x]) + int(s[x:]))
else:
    print(min(int(s[:y]) + int(s[y:]), int(s[:x]) + int(s[x:])))
#