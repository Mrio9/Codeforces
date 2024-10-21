t = int(input())
for _ in range(t):
    n = int(input())
    movie1 = list(map(int,input().split()))
    movie2 = list(map(int,input().split()))
    
    a,b,t1,t2 = 0,0,0,0
    for i in range(len(movie1)):
        if movie1[i] > movie2[i]:
            a += movie1[i]
        elif movie1[i] < movie2[i] :
            b += movie2[i]
        else:
            if movie1[i] == 1:
                t1 += 1
            elif movie1[i] == -1:
                t2 += 1
    while t2:
        if a > b:
            a -= 1
        else:
            b -= 1
        t2 -= 1
    while t1 :
        if a < b:
            a += 1
        else:
            b += 1
        t1 -= 1
        
    print(min(a,b))
    
    