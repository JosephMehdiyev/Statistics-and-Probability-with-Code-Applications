import numpy as np
import matplotlib.pyplot as plt

# These are our parameters
n = 100
p1 = 0.3
p2 = 0.5
p3 = 0.07
numberOfExperiments = n

# We already discussed about binomial distributions. Coin flipping is one of these.
# This function does the experiment size times, saves them in result variable as an array.
result1 = np.random.binomial(n = n,p = p1, size = numberOfExperiments)
result2 = np.random.binomial(n = n,p = p2, size = numberOfExperiments)
result3 = np.random.binomial(n = n,p = p3, size = numberOfExperiments)


#
nn = np.arange(1, n + 1)
plt.figure(figsize=(4.5, 3.5))
plt.plot(nn, np.cumsum(result1) / (nn*n), label='p = 0.3')
plt.plot(nn, np.cumsum(result2) / (nn*n), label='p = 0.5')
plt.plot(nn, np.cumsum(result3) / (nn*n), label='p = 0.3')

plt.legend(loc='upper right')
plt.ylabel(" Head to toss ratio")
plt.xlabel("Number of Experiments")
plt.savefig('src/chapter1/fig1.pgf')
