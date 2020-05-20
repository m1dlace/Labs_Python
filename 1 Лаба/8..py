import random
import math
ar = [int(random.uniform(1, 1000)) for i in range(0, int(random.uniform(1, 10000)))]
n = 2 ** math.ceil(math.log2(len(ar)))
print('После: {0}\n'.format(len(ar)))
[ar.append(random.uniform(1, 1000)) for i in range(len(ar), n)]
print('После: {0}\n'.format(len(ar)))