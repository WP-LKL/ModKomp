#import numpy as np
#from itertools import product

class oscar_recursive:
    def __init__(self): self.name = "Oscar's dynamic"

    def hsum(self,x,h,table,w):
        if h*x in table:
            return table[h*x]
        else:
            if h == 1:
                table[h*x] = np.sum(np.exp(w[-1]*x)+np.exp(-x*w[-1]))
                return table[h*x]
            else:
                table[h*x] = np.exp(w[-h]*x)*(self.hsum(1,h-1,table,w) + self.hsum(-1,h-1,table,w))
                return table[h*x]

    def Z(self,n,w):
        """Dynamic recursive solution"""
        table = {}
        res = self.hsum(1,n-1,table,w) + self.hsum(-1,n-1,table,w)
        return res




