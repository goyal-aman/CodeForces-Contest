
m1, m2, c = map(int, input().split())
total_cononut = (m1 // c) + (m2 // c)
remaining_money = (m1 % c) + (m2 % c)
money_exchange = 0
if remaining_money >= c:
    total_cononut += 1
    money_exchange = c - max(m1 % c, m2 % c)
print(total_cononut, money_exchange)
