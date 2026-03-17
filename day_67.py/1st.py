import numpy as np
# input
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# convert to numpy arrays
A = np.array(A)
B = np.array(B)
# inner product
print(np.inner(A, B))
# outer product
print(np.outer(A, B))
