# ModKomp
Git repository for the class Models for Complex Systems

## Exercise 6: 
1. Create your own subfile (e.g. `group0.py`), with a class (`Group0IsAwesome`). The class must have an attribute `name` (e.g. `self.name = "Group 0s calculator"`) and a method `Z` which takes as input an integer `n` and numpy array `w` with shape `(n-1,)`, and returns the normalization constant `Z(n,w) := sum_{x1, ..., xn} P(x1, ..., xn)`, where P is the joint probability of the Ising model with graph `X1 - X2 - ... - Xn` and energy function `epsilon(x_i, x_{i+1}) = - w_i*x_i*x_{i+1}`.
2. Once you have added your Z function to a class, go to the file `arena.py` and register it, by importing it (`from group0 import Group0IsAwesome`) and adding it to the list of models in the Engine. 

Once you have completed the two above points, make a pull request, and your model will be competing against the rest on Friday. Models are tested on speed for various values of `n`. 

__Important:__ Solutions based on closed form solutions to the Ising problem will not be allowed to compete. Closed forms are of course very good solutions, but the point here is to implement the variable elimination algorithm. 
