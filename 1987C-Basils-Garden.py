t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    time = [0] * (n)
    ans = [0]*(n)
    ans[-1] = arr[-1]
    for i in range(n -2,-1,-1):
        if arr[i] <= arr[i + 1]:
            time[i] =  (arr[i + 1] - arr[i]  + 1) + time[i] + time[i + 1]
        ans[i] = arr[i] + time[i]
        ans[i] = max(ans[i],ans[i+1] + 1)
    print(max(ans))