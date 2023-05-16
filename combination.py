import numpy as np 

# implement your function to combine two numpy arrays 

def combination(arr1, arr2, axis=0):
    # Remove unnecessary dimensions
    arr1, arr2 = np.squeeze(arr1), np.squeeze(arr2)
    
    try:
        # Try to combine the arrays
        return np.concatenate((arr1, arr2), axis=axis)
    except ValueError:
        # If a ValueError is raised, the arrays cannot be combined along the specified axis
        raise ValueError(f"Cannot combine arrays of shape {arr1.shape} and {arr2.shape} along axis {axis}")


if __name__ == "__main__":
    # use this for your own testing!

    pass
