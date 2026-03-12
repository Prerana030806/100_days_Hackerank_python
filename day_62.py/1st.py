import numpy as np
# Read input
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# Convert to numpy array
matrix = np.array(arr)
# Transpose
print(matrix.T)
# Flatten
print(matrix.flatten())
