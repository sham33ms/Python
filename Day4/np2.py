import numpy as np

print(np.zeros(3))              # [0. 0. 0.]
print(np.zeros((2,3)))          # 2x3 array of zeros
print(np.ones(4))               # [1. 1. 1. 1.]
print(np.ones((2,3)))           # 2 rows, 3 columns of ones)

print(np.full((2,3),7))         # 2x3 array filled with 7

print(np.eye(3))                # 3*3 Identity matrix
print(np.eye(5))                # 5*5 Identity matrix
print(np.eye(2,3))              # 2*3 Identity matrix

print(np.arange(1,6))           # [1 2 3 4 5]
print(np.arange(0,10,2))        # [0 2 4 6 8]

print(np.linspace(0,5,6))       # [0. 1. 2. 3. 4. 5.]
print(np.linspace(0,1,5))       # [0.  0.25 0.5  0.75 1.] Creates 5 evenly spaced values between 0 and 1 (inclusive)


# np.zeros(shape)               # All zeros
# np.ones(shape)                # All ones
# np.full(shape, value)         # All filled with specific value
# np.eye(n)                     # Identity matrix
# np.arange(start, stop, step)  # Like range()
# np.linspace(start, stop, num) # Evenly spaced values
