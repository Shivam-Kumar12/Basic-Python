import numpy as np
from matplotlib import pyplot as plt

samplesize =10000
uniform =np.random.rand(samplesize)
normal =np.random.randn(samplesize)
plt.hist(uniform,bins=100)
plt.title('rand:uniform')
plt.show()
plt.hist(normal,bins=100)
plt.title('randn:normal')
plt.show()


