t = int(input())

for _ in range(t):
    n,m = list(map(int,input().split()))
    questions = input()
    arr = {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0}
    ans = 0
    for i in questions:
        arr[i] += 1
    for key,val in arr.items():
        if m > val:
            ans += m - val
    print(ans)