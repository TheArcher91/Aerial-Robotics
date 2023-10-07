import numpy as np
import matplotlib.pyplot as plt

# Part - (e)
np.random.seed(300)

# Part - (a)
rand_var1 = np.random.normal(5, 2, 100000)

# Part - (b)
rand_var2 = np.random.uniform(0, 10, 100000)

# Part - (c)

print("Normal Dist. Mean - ",np.mean(rand_var1) )
print("Normal Dist. SD - ",np.std(rand_var1) )
print("Uniform Dist. Mean - ", np.mean(rand_var2))
print("Uniform Dist. SD - ", np.std(rand_var2))

# Part - (d)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(rand_var1, bins=50, color='blue', alpha=0.7)
plt.title('Histogram of Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(rand_var2, bins=50, color='green', alpha=0.7)
plt.title('Histogram of Uniform Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

