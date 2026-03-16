import re
t = int(input())
for _ in range(t):
    s = input()
    try:
        re.compile(s)
        if re.search(r'\+\+', s) or re.search(r'\*\+', s):
            print(False)
        else:
            print(True)
    except:
        print(False)
