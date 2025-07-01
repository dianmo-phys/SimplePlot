# Read and process data

import numpy as np

def discrete_pdf(data, bins=10, range=None, weights=None):
    """
    Counts probability density function of discrete data.
    
    Parameters:
    - data: array-like, discrete data
    - bins: int, number of bins for the histogram
    """
    counts, bin_edges = np.histogram(data, bins=bins, density=True, range = range, weights=weights)
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    return bin_centers, counts
