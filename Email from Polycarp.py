from collections import Counter

n = int(input())
l =[]
for i in range(n):
    l.append([input(), input()])

for ele in l:
    dict1 = dict(Counter(ele[0]))
    dict2 = dict(Counter(ele[1]))

    if set(dict1)!=set(dict2):
        print('NO')
        break

    for i in set(dict1):
        if dict1[i] > dict2[i]:
            print('NO')
            break
    else:
        print('YES')


    # from collections import Counter
# n = int(input())
# l = []
# for _ in range(n):
#     dict1 = dict(Counter(input()))
#     dict2 = dict(Counter(input()))
#     main_dict = {
#         'dict1': dict1,
#         'dict2': dict2
#     }
#     l.append(main_dict)
# # t = l
# # print('t = ',t)
# # for i in l:
# #     print(i)
#
#     #dict1 = dict(Counter(input()))
#     #dict2 = dict(Counter(input()))
#     # print(dict1, dict2)
# for i in l:
#     if i['dict1']!=i['dict2']:
#         print('NO')
#         exit()
#     for j in set(i['dict1']):
#         if i['dict1'][j] < i['dict2'][j]:
#             print('NO')
#             exit()
#     print('YES')