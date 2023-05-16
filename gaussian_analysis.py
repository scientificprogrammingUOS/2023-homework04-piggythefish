import numpy as np

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    # Check that all arguments are of type int or float
    if not all(isinstance(arg, (int, float)) for arg in [loc, scale, lower_bound, upper_bound]):
        raise ValueError("All arguments must be of type int or float.")
    # Check that lower_bound is smaller than upper_bound
    if not lower_bound < upper_bound:
        raise ValueError("lower_bound must be smaller than upper_bound.")

    # Draw 100 samples from a Gaussian distribution
    samples = np.random.normal(loc, scale, 100)

    # Filter out values below lower_bound and above upper_bound
    samples = samples[(samples > lower_bound) & (samples < upper_bound)]

    # Calculate the mean and standard deviation
    mean = np.mean(samples)
    std = np.std(samples)

    return mean, std


if __name__ == "__main__":
    # use this for your own testing!
    gaussian_analysis(loc=3, scale=5, lower_bound=1, upper_bound=5)
    
