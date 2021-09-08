#single neuron with NumPy

import numpy as np

inputs = [1,2,3,2.5]
weights = [.2,.8,-.5,1]
bias = 2

outputs = np.dot(weights, inputs) + bias

print(outputs)

