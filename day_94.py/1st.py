import numpy as np
a , b = map(int , input().split())
arr = np.array([list(map(int,input().split())) for i in range(a)])
print(np.max(np.min(arr,axis=1)))
