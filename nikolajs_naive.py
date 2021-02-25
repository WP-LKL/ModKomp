import numpy as np
from itertools import product

class nikolajs_naive:
    def __init__(self): self.name = "Nikolajs naive"

    def _P(self, x, w):
        """Unnormalized density in x"""
        x = np.array(x)
        return np.exp(-w*x[1:].dot(x[:-1]))

    def Z(self, n, w):
        """Compute the normalization constant for a choice of n and w"""
        return sum(self._P(x, w) for x in product([-1, 1], repeat=n))
