from collections import defaultdict
n, m = map(int, input().split())
position = defaultdict(list)
for i in range(1, n + 1):
    word = input().strip()
    position[word].append(i)
for i in range(m):
    word = input().strip()
    if word in position:
        print(*position[word])
    else:
        print(-1) 
