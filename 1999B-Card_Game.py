t = int(input())

for _ in range(t):
    a, b,c,d = map(int, input().split())
    ans = 0
    
    if (a > c and b >= d )or (a >= c and b > d):
        ans += 2
    if (a > d and b >= c )or (a >= d and b > c):
        ans += 2
    
    print(ans)