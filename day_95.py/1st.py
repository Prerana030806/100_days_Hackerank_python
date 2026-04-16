import numpy as np 
n , m = map(int, input().split())
arr = np.array([list(map(int,input().split())) for _ in range(n)])
col_sum = np.sum(arr,axis=0)
result = np.prod(col_sum)
print(result) 
