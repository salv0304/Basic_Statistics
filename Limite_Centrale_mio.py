#Plot of the (normalized) sum of n uniform random variables that results in a (normalized) gaussian distribution

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm 


#Generate and plot a single uniform random variable
uniform = np.random.uniform(low=-1, high=1, size=10000)

plt.hist(uniform, bins=30, color='skyblue', edgecolor='black', density=True) #density normalize the histogram
plt.xlabel('Values')
plt.ylabel('Density')
plt.title('Histogram of a Single Uniform Random Variable')
plt.show()

# Define the Gaussian (normal) distribution for comparison
mu= 0 #mean
sigma= 1 # standard deviation
x = np.linspace(-3.5, 3.5, 10000)
gaussian = norm.pdf(x, mu, sigma)  #PDF of the standard normal distribution

#Generate n uniform random variables
n = 100
n_uniform = np.random.uniform(low=-1, high=1, size=(n,10000)) 

#Sum of n uniform random variables and normalizing the result
result = np.sum(n_uniform, axis=0)
normalized_sum = (result - np.mean(result)) / np.std(result)

#Plotting the histogram of the normalized sum and the Gaussian curve for comparison
plt.hist(normalized_sum, bins=30, color='green', edgecolor='black', alpha=0.6, density=True, label="Normalized sum of uniforms")
plt.plot(x, gaussian, 'b', label='Standard normal distribution')
plt.xlabel('Values')
plt.ylabel('Density')
plt.title(f'Sum of {n} uniform random variables')
plt.show()
