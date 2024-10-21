t = int(input())
arr = [0]*100010
 
for _ in range(t):
    n = int(input())
    arr[1:n+1] = map(int, input().split())
    if n == 2:
        print(min(arr[1], arr[2]))
    else:
        ans = min(arr[1], arr[2])
        for i in range(1, n-1):
            tmp = sorted(arr[i:i+3])
            ans = max(ans, tmp[1])
        print(ans)