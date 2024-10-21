t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    n = n % 30
    if n == 1 or n == 4 or n == 7 or n == 17:
        ans += 1
    elif n == 2:
        ans += 2
    print(ans)