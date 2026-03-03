import numpy as np
N = int(input())
A = np.array([list(map(int, input().split())) for _ in range(N)])
B = np.array([list(map(int, input().split())) for _ in range(N)])
result = np.dot(A, B)
print(result) 
