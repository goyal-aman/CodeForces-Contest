n, x, y = map(int, input().split())
s = (input()[n - x:])
print(s.count('1') + (-1 if (s[-y - 1] == '1') else 1))
