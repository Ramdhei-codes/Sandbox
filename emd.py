import numpy as np
from scipy.stats import wasserstein_distance

# Define two probability distributions (arrays)
distribution1 = np.array([0.2, 0.3, 0.5])
distribution2 = np.array([0.1, 0.6, 0.3])

# Calculate Earth Mover's Distance
emd_distance = wasserstein_distance(distribution1, distribution2)

print(f'Earth Mover\'s Distance: {emd_distance}')
