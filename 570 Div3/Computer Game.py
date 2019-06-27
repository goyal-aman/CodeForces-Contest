"""
1.phele check kro ki given charge k, n*a se jyada h ya nh
        if yes, then print n, and move on to next query
        if no, then goto step 2
2. calculate charge needed by k - n*a,
        ye btaega ki kitne charge ki kaami pad rhi h jab hum sare turn a ki hisab se chl rhe h

    charge_needed bta rha h ki kitna charge kam h, b ham bari bari har turn ke lie a move ko b move se replace krna chate h,
    jisse battry ka charge  a-b se badega,

3. pta kro ki kitni bar a wale move ko b se replace krna padega, - (turn)

4. agr turn needed n se bada h to print -1, vrna print turn-n

"""

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