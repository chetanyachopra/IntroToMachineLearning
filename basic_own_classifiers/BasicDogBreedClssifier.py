import numpy as np
import matplotlib.pyplot as plt

labs=500
greyhounds=500

labs_height=24 + 4 * np.random.randn(labs)
greyhounds_height=28+ 4 * np.random.randn(greyhounds)

#visualizee in hostogram

plt.hist([greyhounds_height,labs_height],stacked=True,color=['r','b'])
plt.show()