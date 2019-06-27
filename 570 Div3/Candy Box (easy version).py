
import sys
for _ in range(int(input())):
    n = int(sys.stdin.readline())
    li = list(map(int, sys.stdin.readline().split()))
    s = [0] * n
    for i in li:
        s[i - 1] =s[i - 1]+ 1
    s.sort(reverse=True)
    m = 2 * (10 ** 6) + 1
    max_gs = 0
    for i in s:
        m = max(min(m - 1, i), 0)
        max_gs =max_gs+ m

    print(max_gs)


# for _ in range(int(input())):
#     n = int(input())
#     li = list(map(int, input().split()))
#     s = [0] * n
#     for i in li:
#         s[i - 1] =s[i - 1]+ 1
#     s.sort(reverse=True)
#     m = 2 * (10 ** 6) + 1
#     max_gs = 0
#     for i in s:
#         m = max(min(m - 1, i), 0)
#         max_gs =max_gs+ m
#
#     print(max_gs)
