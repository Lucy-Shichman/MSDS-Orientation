import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

normal = np.random.normal(100,10,300)
plt.hist(normal)
plt.show()

binomial = np.random.binomial(1,0.3,10)
plt.hist(binomial)
plt.show()

poisson=np.random.poisson(5,1000)
plt.hist(poisson)
plt.show()

