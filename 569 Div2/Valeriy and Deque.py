elements, query = map(int, input().split())
s = list(map(int, input().split()))

mx = max(s)

results = []
# print(results)
while s[0] != mx:
    results.append((s[0],s[1]))
    if s[0] > s[1]:
        s[0], s[1] = s[1], s[0]
    temp = s.pop(0)
    s.append(temp)
# print(results)
# print(s)
for _ in range(query):
    num = int(input())
    if num <= len(results):
        print(*results[num-1])
    else:
        print(mx, s[(num - 1 - len(results))%(elements - 1) + 1])







# elements , query = map(int, input().split())
# s = list(map(int, input().split()))
# holder = []
# max_s = max(s)
# maxindex = s.index(max_s)
#
# while s[0] != max_s:
#     a,b = s[0],s[1]
#     holder.append((a,b))
#     s[0],s[1]= min(s[0],s[1]), max(s[0],s[1])
#     temp = s.pop(0)
#     s.append(temp)
#
# # print(holder)
# # print(s)
# for _ in range(query):
#     present_query = int(input())
#     if present_query< maxindex+1:
#         print(*holder[present_query-1])
#
#     else:
#         print(max_s, s[(present_query - (maxindex + 1))%(elements-1) + 1] )
#
#
# #
# # for _ in range(query):
# #     l = input()
#
#
# # 1 2 9 3
# # 2 9 3 1
# # 9 3 1 2
# # 9 1 2 3
# # 9 2 3 1
# # 9 3 1 2
# # 9 1 2 3
# # 9 2 3 1
# #
# # elements,num_query = map(int, input().split())
# # l = list(map(int, input().split()))
# # i = 0
# # while l[0] != max(l):
# #     if l[i] > l[i+1]:
# #
# #
# # for _ in range(num_query):
# #     query = int(input())
# #     if query>= elements:
# #         print(max(l), l[query%elements - 1] )
# #
# #
# # a,b=map(int,input().split())
# # c=list(map(int,input().split()))
# # d=[]
# # e=c[0]
# # z=max(c)
# # ff=[]
# # for i in c[1:]:
# #     ff.append(min(e,i))
# #     e=max(e,i)
# #     d.append(e)
# #     #ff.append(min(e,i))
# # for _ in range(b):
# #     l=int(input())
# #     if l<a:
# #         if l==1:
# #             print(c[0],c[1])
# #         else:
# #             print(d[l-2],c[l])
# #     if l>=a:
# #         l=l%(a-1)
# #         print(z,ff[l-1])
# #
#
# # n, q = map(int, input().split())
# # s = list(map(int, input().split()))
# # query = []
# # for _ in range(q):
# #     query.append(int(input()))
# #
# # if  q > 0:
# #     for i in range(1,query[-1] + 1):
# #         if i in query:
# #             print(s[0], s[1])
# #
# #         if s[0] > s[1]:
# #             temp = s.pop(1)
# #             s.append(temp)
# #         else:
# #             temp = s.pop(0)
# #             s.append(temp)
