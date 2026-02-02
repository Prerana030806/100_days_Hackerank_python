n = int(input())
for i in range(n):
    s = input().strip()
    if len(s) == 10 and s.isdigit() and s[0] in '789':
        print("YES")
    else:
        print("NO")
