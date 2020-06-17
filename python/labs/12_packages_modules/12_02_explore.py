'''
Do some research on other popular python packages and what the are used for.
Feel free to import them and play around a little.

'''
import numpy as np

array_1 = np.array([[1, 3, 5], [0.5, 0.7, 0.9]])
array_2 = np.array([[10, 15, 20]])

print(np.concatenate((array_1, array_2), axis=0))
