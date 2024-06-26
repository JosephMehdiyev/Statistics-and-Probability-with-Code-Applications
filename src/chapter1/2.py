import numpy as np
import matplotlib.pyplot as plt

n = 100
numberOfExperiments = n
# This is a numpy thing. It will be used for generating probability distributions.
# Basically makes the probability possible
rng = np.random.default_rng()

# Here we draw random integers in interval (1,6) for n times, and repeat the process "numberOfExperiment" times 
result = rng.integers(low = 1, high = 7, size = (n, numberOfExperiments) )

# This loop counts the number of capA we get in one experiment, and loops through the total experiments.
totalCapA = []
for element in result:
    # Outputs Bool values depending on the input array, i.e [2,4,6]
    initialCapA = np.isin(element, [2,4,6])
    # Number of Bool values.
    totalCapA.append(initialCapA.sum())

# Repeat the same process for capB and capAB
totalCapB = []
for element in result:
    initialCapB = np.isin(element, [1,2,3,4])
    totalCapB.append(initialCapB.sum())
totalCapAB = []
for element in result:
    initialCapAB = np.isin(element, [2,4])
    totalCapAB.append(initialCapAB.sum())

# A simple array [1,2,...,n]
experimentOrder = np.arange(1,n+1,1)


plt.figure(figsize=(6, 3.5))

# The fancy expressions here just takes the average value. 
# X axis is "experimentOrder" while the Y axis is our fancy expressions.
plt.plot(experimentOrder, np.cumsum(totalCapA)/(experimentOrder *n), label = "$\widehat{P}(A)$")
plt.plot(experimentOrder, np.cumsum(totalCapB)/(experimentOrder *n), label = "$\widehat{P}(B)$")
plt.plot(experimentOrder, np.cumsum(totalCapAB)/(experimentOrder *n), label = "$\widehat{P}(AB)$")
plt.plot(experimentOrder, np.multiply(np.cumsum(totalCapA),np.cumsum(totalCapB))/((experimentOrder *n)*(experimentOrder *n)), label = "$\widehat{P}(A)\widehat{P}(B)$")

plt.ylabel("Average ratio")
plt.xlabel("Number of Experiments")
plt.legend(loc='upper right')
plt.savefig('src/chapter1/fig2.pgf')
