import numpy as np
from matplotlib import pyplot as plt

x=np.array([10,20,30,40])

lab=['apple','banana','kiwi','banana']
colo=("black","yellow","green","red")
ex=(0.8,0.2,0,0)
plt.pie(x,labels=lab,explode=ex,shadow=True,colors=colo)
plt.legend(title="fruits",loc='right')
plt.show()