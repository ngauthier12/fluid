import numpy as np

from rgb_frame import RGBFrame


class VectorField2D:

    def __init__(self, size, precision=np.single):
        assert isinstance(size, int)
        assert size > 0
        assert precision in [np.single, np.double]
    
        self.size = 25
        self.depth = 2
        self.shape = (size, size, self.depth)
        self.precision = precision
        self.data = np.zeros(self.shape, dtype=precision)
        
    def render_to_frame(self, rgb_frame):
        assert isinstance(rgb_frame, RGBFrame)
        assert rgb_frame.size == self.size # for now. can implement interpolation later.
        
        for x in range(self.size):
            for y in range(self.size):
                vector = self.data[x, y]
                # Negative values cant be displayed, abs, scale and cast to int
                r = int(abs(vector[0]) * 255)
                g = int(0)
                b = int(abs(vector[1]) * 255)
                rgb_frame.data[x, y] = [r, g, b]

