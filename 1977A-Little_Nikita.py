t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    ans = ""
    temp = n - m
    if n == m:
        print("YES")
    elif n < m:
        print("NO")
    elif temp % 2 == 0:
        print("YES")
    else:
        print("NO")