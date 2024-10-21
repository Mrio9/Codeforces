t = int(input())
for _ in range(t):
    p1,p2,p3 = map(int , input().split())
    ans = 0
    k = 1
    if p1 == p2 == p3 == 0:
        print(0)
    elif p1 == p2 == p3 and p1 % 2:
        print(-1)
    else:
        t1 = max(p1,p2,p3)
        t2 = min(p1,p2,p3)
        t3 = p1 + p2 + p3 - t1 - t2
        ans += t2
        t1 -= t2
        if t1 >= t3:
            ans += t3
            t1 -= t3
            if t1 % 2 == 0:
                k = 1
            else:
                k = 0
                print(-1)
        else:
            ans += t1
            t1 = abs(t1-t3)
            if t1 % 2 == 0:
                ans += t1 // 2
            else:
                k = 0
                print(-1)
        if k:
            print(ans)
            