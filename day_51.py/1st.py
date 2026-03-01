A = set(input().split())
n = int(input())
result = True
for i in range(n):
    other_set = set(input().split())
    if not (A > other_set):  # strict superset check
        result = False
        break
print(result)
