import numpy as np


class RGBFrame:

    def __init__(self, size):
        assert isinstance(size, int)
        assert size > 0
    
        self.size = 25
        self.depth = 3
        self.shape = (size, size, self.depth)
        self.data = np.zeros(self.shape, dtype=np.uint8)

