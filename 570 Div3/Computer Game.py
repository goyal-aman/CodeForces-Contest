for _ in range(int(input())):
    k, n, a, b = map(int, input().split())
    if k>n*a:
        print(n)
        continue
    else:
        charge_needed = k - n*a
        diff = a - b
        turn = -(charge_needed)//diff +1
        if n-turn>=0:
            print(n-turn)
        else:
            print(-1)