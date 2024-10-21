t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    
    arr.sort()
    ans = 0
    for i in range(len(arr) -1):
        ans += 2*arr[i] - 1
    print(ans)