import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


# Generate an array with 1000 float elements, evenly spaced.
X = np.linspace(-5,5, num = 1000)
plt.figure(figsize=(6, 3.5))
# norm.pdf(x) gives the value of p.d.f of N(0,1) at x.
plt.plot(X, norm.pdf(X), label = "$f_X(x)$")
# We implement the equation we derived.
plt.plot(X, norm.pdf(np.log(X))/X, color = 'orange', label = "$f_Y(y)$" )
plt.title(r"Graph 1.")
plt.legend(loc='upper right')
plt.ylabel("p.d.f")
plt.xlabel("r.v")

# Now we draw the histogram plot
rng = np.random.default_rng() # initialize
totalPoints = 10000 # total number we will randomly select
arrayX = rng.normal(loc = 0, scale = 1, size = totalPoints) # array of selected numbers
barSize = 200 # number of the bars
plt.hist(np.exp(arrayX), bins = barSize, range = (0,6),density = True, color = 'g', alpha = 0.6 )
plt.savefig('src/chapter2/fig1.pgf')


