library(ggplot2)

# Normal Distribution
hist(rnorm(1000)) # k=1000 random values

# Binomial Distribution
hist(rbinom(10,100,0.5)) # n=10 trials, size= 1000 samples, p=0.1

# Poisson Distribution
hist(rpois(100,lambda = 10))

