import numpy as np
from itertools import product

class nikolajs_naive:
    def __init__(self): self.name = "Nikolajs naive"

    def _P(self, x, w):
        """Unnormalized density in x"""
        x = np.array(x)
        return np.exp(-np.sum(w*x[1:]*(x[:-1])))

    def Z(self, n, w):
        """Compute the normalization constant for a choice of n and w
        n: Integer
        w: np.array, shape = (n-1,)
        """
        return sum(self._P(x, w) for x in product([-1, 1], repeat=n))
