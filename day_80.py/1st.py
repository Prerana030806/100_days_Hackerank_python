import re
n = int(input())
inside_block = False
for i in range(n):
    line = input()
    
    if '{' in line:
        inside_block = True

    if inside_block:
        matches = re.findall(r'#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?', line)
        for m in matches:
            print(m)
    if '}' in line:
        inside_block = False
