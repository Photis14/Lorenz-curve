import numpy as np
from matplotlib import pyplot as plt

data = np.load('pop2010.npy') 
data.sort()  

def plot_lorenz(data):  
    sumsum = data.cumsum() / data.sum() 
    insert = np.insert(sumsum, 0, 0)
    return insert

plt.plot(np.linspace(0.0, 1.0, plot_lorenz(data).size,), plot_lorenz(data), color="red", linestyle="dashed")
plt.plot([0,1], [0,1], color="green")
plt.title("Common Wealth")
plt.xlabel("Number of Countries")
plt.ylabel("Total Contribution")
plt.savefig("population-lorenz.png", dpi=200)
plt.show()



#sources
#https://matplotlib.org/2.0.2/users/pyplot_tutorial.html



