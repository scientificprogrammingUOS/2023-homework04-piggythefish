import numpy as np

# implement the function strange pattern

def strange_pattern(shape):
    pattern = np.full(shape, False)
    pattern[::3, ::3] = True
    pattern[1::3, 2::3] = True
    pattern[2::3, 1::3] = True
    return pattern

if __name__ == "__main__":
    # use this for your own testing!
    print(strange_pattern((8,8)))
