import sys
input = sys.stdin.readline
n = int(input())
string = input().rstrip()
s = [[] for i in range(26)]
# print(s)
# print(s) #debug
for i in range(n):
    s[ord(string[i])-ord('a')].append(i)
# print(s) #debug
# print(s)
for _ in range(int(input())):
    name_li = [0]*26
    name = input().rstrip()
    for i in name:
        name_li[ord(i) - ord('a')]+=1
    # print(name_li)
    ans = 0
    for j in range(26):
        if name_li[j]>0:
            ans = max(ans, s[j][name_li[j]-1])
    print(ans+1)



'''__________my sol'''
# import sys
# n = int(sys.stdin.readline().rstrip())
# s = sys.stdin.readline().rstrip()
#
# for _  in range(int(input())):
#     s2 = list(s)
#     name = sys.stdin.readline().rstrip()
#     temp_t = 0
#     for i in name:
#         t = s2.index(i)
#         s2[t] = '0'
#         if t>temp_t:
#             temp_t=t
#     print(temp_t+1)
