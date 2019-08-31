from collections import Counter


def koutsu(li):
    li = max(list(dict(Counter(li)).values()))

    if li >= 3:
        return 0
    elif li == 2:
        return 1
    else:
        return 2


def shun(li):
    li = sorted(li, key=lambda x: x[1])
    if li[0][1]==li[1][1]==li[2][1]:
        p = (min(abs(int(li[0][0]) - int(li[1][0])), abs(int(li[1][0]) - int(li[2][0])),
                 abs(int(li[2][0]) - int(li[1][0]))))
        if (int(li[0][0]) + int(li[1][0]) + int(li[2][0]))%3==0:
            return 0
        elif p==1:
            return 1
        else:
            return 2
    else:
        return 100

        # t = min(abs(int(li[0][0]) - int(li[1][0])),abs(int(li[1][0]) - int(li[2][0])),abs(int(li[2][0]) - int(li[1][0])))

        # return max(min(t-1,2),0)
    # else:
    #     return max(abs(int(li[0][0]) - int(li[1][0])),abs(int(li[1][0]) - int(li[2][0])),abs(int(li[2][0]) - int(li[1][0])))


n = list(input().split())
print(koutsu(n))
print(shun(n))
print(min(koutsu(n), shun(n)))
