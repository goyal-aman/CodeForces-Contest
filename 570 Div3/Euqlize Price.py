q = int(input())
for _  in range(q):
    n,k = map(int, input().split())
    s = list(map(int, input().split()))
    min_s = min(s)
    max_s = max(s)
    if min_s+k < abs(max_s-k) :
        print(-1)
        continue
    else:
        print(min_s+k)

# '''
# 1. a = min(<given_list>)
# 2. nai list with all the elements <a> size n
# 3.agr diff of a and max(<given_list>)>k, a=a+1, goto 2
# 4. nai list with all elements a, agr a< (k - (a-min_s) ), then a  = a+ (k - min_s )
#
# '''
#
# q = int(input())
# for _ in range(q):
#     n,k = map(int, input().split())
#     s = list(map(int, input().split()))
#     max_s = max(s)
#     min_s = min(s)
#     avg = sum(s)/n
#     if max_s-min_s> 2*k:
#         print(-1)
#         break
#
#     a = min_s
#     run = True
#     while run:
#         if abs(a-max_s)>k:
#             a+=1
#             continue
#         new_li = [a]*n
#         # print(new_li)
#         if a < (k-min_s):
#
#