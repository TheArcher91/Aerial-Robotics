from math import cos , exp
import numpy as np
import matplotlib.pyplot as plt

x = []
y = []

z = 2 * np.pi
i = -z
while i < z :
    x.append(i)
    y.append(cos(i) * exp(i))
    i = i + 0.01

plt.plot(x,y)

plt.xlabel('X axis') 
 
plt.ylabel('Y axis') 
    
plt.title('Plot of X vs Y') 
 
plt.show() 
