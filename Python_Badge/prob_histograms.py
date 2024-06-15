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

# Visually Demonstrate (use histograms) to show that the 
# Binomial and Normal distributions converge in the large N limit.

normal_small = np.random.normal(0,0.1,100) # mean=0, sd=0.1, size=100
plt.hist(normal_small,color="green")
plt.show()

binomial_small = np.random.binomial(10,0.5,100) # trials=10, prob=0.5, tested=100) 
plt.hist(binomial_small, color="green")
plt.show()

normal_large = np.random.normal(0,0.1,10000)
plt.hist(normal_large,color="red")
plt.show()

binomial_large = np.random.binomial(10000,0.5,100)
plt.hist(binomial_large,color="red")
plt.show()

# "The central limit theorem (CLT) states that as the number of trials
# (\(n\)) increases, a binomial distribution with a probability of success 
# (\(p\)) gets closer to a normal distribution."