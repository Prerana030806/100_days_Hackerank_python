import numpy as np 
n = int(input())
a = []
for _ in range(n):
  a.append(list(map(float,input().split())))
mat = np.array(a)
det = 1
for i in range(n):
  det *= mat[i][i]
print(round(np.linalg.det(mat),2))
