t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(input())
    dist = set()
    for i in arr:
        if i not in dist:
            dist.add(i)
    temp = list(sorted(dist))
    dic = {}
    m = len(temp)
    for i in range(m):
        dic[temp[i]] = temp[m-i-1]
    ans = ""
    for i in arr:
        ans += dic[i]
    print(ans)