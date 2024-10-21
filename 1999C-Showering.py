t = int(input())

for _ in range(t):
    tasks,showertime,daytime = map(int,input().split())
    arr = []
    diff = 0
    for _ in range(tasks):
        t1,t2  = map(int,input().split())
        arr.append([t1,t2])
    if arr[0][0] >= showertime or daytime - arr[-1][-1] >= showertime:
        print("YES")
    else:
        for i in range(tasks - 1):
            diff = max(diff,arr[i+1][0] - arr[i][1])
        
        if diff >= showertime:
            print("YES")
        else:
            print("NO")
    
    