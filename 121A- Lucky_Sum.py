l,r = map(int,input().split())
arr = []

def help(num):
    if num > 10000000000:
        return
    arr.append(num)
    help(num*10 + 4)
    help(num*10 + 7)
help(0)
arr.sort()
ans = 0
temp = 0
ind = 1

while l <= r :
    while arr[ind] < l:
        ind += 1
    if arr[ind] < r:
        temp = arr[ind] - l + 1
        ans += arr[ind] * temp
        l += temp
        ind += 1
    else:
        ans += arr[ind] * (r - l + 1)
        break
print(ans)