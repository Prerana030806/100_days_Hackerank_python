import numpy as np
N, M, P = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(N)]
arr2 = [list(map(int, input().split())) for _ in range(M)]
np_arr1 = np.array(arr1)
np_arr2 = np.array(arr2)
result = np.concatenate((np_arr1, np_arr2), axis=0)
print(result)
