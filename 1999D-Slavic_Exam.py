t = int(input())

for _ in range(t):
    string = input()
    substring = input()
    n = len(string)
    m = len(substring)
    found = False

    for i in range(n - m + 1):
        if all(string[i + j] == substring[j] or string[i + j] == '?' for j in range(m)):
            string = string[:i] + substring + string[i + m:]
            found = True
            break
    
    if found:
        print("YES")
        arr = []
        for i in string:
            if i != "?":
                arr.append(i)
            else:
                arr.append('a')
        print(''.join(arr))
    else:
        print("NO")
