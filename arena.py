from nikolajs_dummy import NikolajsDummyCalculator
from rasmus import rasmus_simple, rasmus_brute, rasmus_numba
from oscar import oscar_dynamic


class DummyEngine():
    def __init__(self, models): self.models = models
    def is_valid(self):
        """
        For every model, check if it has a callable function .Z and an attribute .name
        """
        for m in self.models:
            if hasattr(m, "Z") and callable(getattr(m, "Z")) and hasattr(m, "name"):
                print(f"Model '{m.name}' is valid.")

#TODO: Import your model class (e.g. NikolajsDummyCalculator) and add it to the list of models
E = DummyEngine(models=[
    NikolajsDummyCalculator(),
    rasmus_simple(),
    rasmus_brute(),
    rasmus_numba(),
    oscar_dynamic()
    ])
# We print all valid models
E.is_valid()
