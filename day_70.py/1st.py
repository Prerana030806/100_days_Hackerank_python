import re

for _ in range(int(input())):
    uid = input()
    
    # Check all conditions together
    if (len(uid) == 10 and
        uid.isalnum() and
        len(set(uid)) == 10 and
        len(re.findall(r'[A-Z]', uid)) >= 2 and
        len(re.findall(r'\d', uid)) >= 3):
        
        print("Valid")
    else:
        print("Invalid")
