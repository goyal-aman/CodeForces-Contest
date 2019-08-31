n = int(input())
d = {
    1:"A",
    2:"C",
    3:'B',
    0:'D'
}
li = []
for i in range(3):
    z = (n+i)%4
    li.append(f"{i} {d[z]}")
# print(li)
print(sorted(li, key=lambda x: x[2])[0])