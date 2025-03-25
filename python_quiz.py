# section 2 quiz 
# Law of large numeber Quiz

import numpy as np
from numpy.random import randn

N = 1000
count = 0
for i in randn(N):
    if 1 >= i >= -1:
        count = count + 1 
mean_value = count / N
print(mean_value)
print(count)
