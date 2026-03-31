import numpy as np

n, m = map(int, input().split())
arr = np.array([list(map(int, input().split())) for i in range(n)])

np.set_printoptions(legacy='1.13')

print(str(np.mean(arr, axis=1)).replace('  ', ' ').replace('[ ', '['))
print(str(np.var(arr, axis=0)).replace('  ', ' ').replace('[ ', '['))
print(np.std(arr))
