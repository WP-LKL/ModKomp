import numpy as np

class rasmus_simple:
    def __init__(self): self.name = "Rasmus' fast implementation"
        
    def Z(self, n, w):
        # Much faster than native python loop
        return 2*np.prod(np.exp(omega)+np.exp(-omega))
    
import numba as nb
class rasmus_numba:
    def __init__(self): 
        self.name = "Rasmus' fast implementation"
        self.par_Z(np.random.randn(100)) # Init JIT for serial
        self.ser_Z(np.random.randn(1000)) # Init JIT for parallel
    
    def Z(self, n, w):
        # Depending on size, serial or parallel may be best. 
        # crossover point found by profiling
        return (self.ser_Z if (len(w) < 375) else self.par_Z)(w)
       
    @staticmethod
    @nb.njit("f8(f8[:])", fastmath=True, parallel=True)
    def par_Z(w):
        return 2*np.prod(2*np.cosh(w))
    
    @staticmethod
    @nb.njit("f8(f8[:])", fastmath=True, parallel=False)
    def ser_Z(w):
        return 2*np.prod(2*np.cosh(w))
    
class rasmus_brute:
    def __init__(self): self.name = "Rasmus' vectorized brute implementation"
        
    def Z(self, n, w):
        # generate all states
        comb = np.arange(2**n)
        x = comb[None,:] & (1 << np.arange(n))[:,None]
        x = (x > 0) * 2 - 1
        
        # calculate all interactions and sum total energy of each state vector
        exponents = np.sum(-omega[:,None]*x[:-1]*x[1:], axis=0)
        return np.sum(np.exp(exponents))
