import re
t = int(input())
pattern = r'^[+-]?\d*\.\d+$'
for _ in range(t):
    s = input()
    if re.match(pattern, s):
        print(True)
    else:
        print(False)
