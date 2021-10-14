from scipy import misc
import matplotlib.pyplot as plt

racoon = misc.face()

row = [[x * 2, 0, 0] for x in range(128)]
test = [row for x in range(128)]

plt.imshow(test) 
plt.show()
