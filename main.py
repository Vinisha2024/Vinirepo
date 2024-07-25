#LINE GRAPH
'''import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([2,20])
ypoints = np.array([4,7])
plt.plot(xpoints,ypoints)
plt.show()'''

import matplotlib.pyplot as plt
import numpy as np
f1 = {'family':'serif','color':'red','loc':'left'}
xpoint = np.array([2,4,6,9,10])
ypoint = np.array([5,9,7,6,10])
plt.plot(xpoint,ypoint,marker = '.',color = "blue",ms=12,mec="blue",mfc="red",ls = 'dotted')
plt.title("GRAPH")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(color="green",ls="dashed")
plt.show()

