from collections import deque
t = int(input())
for i in range(t):
    n = int(input())
    blocks = deque(map(int, input().split()))
    last = float('inf')
    while blocks:
        if blocks[0] >= blocks[-1]:
            pick = blocks.popleft()
        else:
            pick = blocks.pop()
        if pick > last:
            print("No")
            break
        last = pick
    else:
        print("Yes")
