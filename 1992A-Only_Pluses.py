t = int(input())

for _ in range(t):
    arr = list(map(int,input().split()))
    temp = sorted(arr)
    for i in range(5):
        temp = sorted(temp)
        temp[0] += 1
    print(temp[0]*temp[1]*temp[2])