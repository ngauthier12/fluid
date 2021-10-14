import matplotlib.pyplot as plt

from vector_field_2d import VectorField2D
from rgb_frame import RGBFrame


simulation_size = 64
field = VectorField2D(size=simulation_size)
frame = RGBFrame(size=simulation_size)

field.render_to_frame(frame)

plt.imshow(frame.data)
plt.show()
