from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    want = list(map(int,input().split()))
    ans = 0
    q = deque()
    for i in arr:
        q.append(i)
    i = 0
    while i < n:
        if q[i] > want[i]:
            ans += 1
            q.pop()
            q.append(want[i])
            q = deque(sorted(q))
        i += 1
    print(ans)