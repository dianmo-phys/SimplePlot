# Plot using matplotlib

import numpy as np
import matplotlib.pyplot as plt
import data_process as dp

with open('test.dat', 'r') as f:
    data = np.loadtxt(f, skiprows=0)
    X = data[:, 0]
    Y = data[:, 1]

# Use the custom style
plt.style.use('../style/prl.mplstyle')  

# Plot lines
plt.figure()
plt.plot(X, Y, label='Data Line', color='blue', linestyle='-', linewidth=1.5, marker=None)
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('test_line.png')

# Plot scatter
plt.figure()
plt.scatter(X, Y, label='Data Points', color='red', marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('test_scatter.png')

# Plot probability
plt.figure()
bin_centers, counts = dp.discrete_pdf(Y, bins=20)
plt.plot(bin_centers, counts, color='black', linestyle='-', linewidth=1.5, marker=None)
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('test_probability.png')