test = int(input())

while test:
  test -= 1
  n = int(input())
  s = input()
  print(n,s)
  if n == 1:
    print('YES')
  else:
    i = 1
    ans = 1
    for i in range(0,n,i+3):
      if i == n-1:
        ans = 0
      else:
        if s[i] != s[i+1]:
          ans = 0
          i += 3
      if ans:
        print('YES')
      else:
        print('NO')
      break