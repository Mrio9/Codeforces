n = int(input())
while n:
    arr = list(input().split())
    a = int(arr[0])
    b = int(arr[1])
    c = int(arr[2])
    t1 = max(a,b,c)
    t2 = min(a,b,c)
    print(a+b+c-t1-t2)
    n -= 1