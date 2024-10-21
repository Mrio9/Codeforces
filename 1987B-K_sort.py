t = int(input())


for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans  = 0
    maxdiff = 0
    for i in range(1,n):
        if arr[i] < arr[i - 1]:
            ans += arr[i-1] - arr[i]
            maxdiff = max(maxdiff,arr[i-1] - arr[i])
            arr[i] = arr[i-1]
    ans += maxdiff
    print(ans)