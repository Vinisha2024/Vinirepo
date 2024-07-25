import numpy as np
import matplotlib.pyplot as plt
#1st plot
x1 = np.array([2,3,5,6,7])
y1 = np.array([1,4,5,6,8])
plt.subplot(2,2,1)
plt.plot(x1,y1,marker = '.',color = "blue",ms=12,mec="blue",mfc="red",ls = 'dotted')
#2ndplot
x2= np.array([10,40])
y2= np.array([5,6])
plt.subplot(2,2,2)
plt.plot(x2,y2,marker = '.',color = "green",ms=12,mec="blue",mfc="yellow",ls = ':')
#3rdplot
x3 = np.array([150,250])
y3 = np.array([70,30])
plt.subplot(2,2,3)
plt.plot(x3,y3,marker = '.',color = "orange",ls = '--')
#4thplot
x4 = np.array([6,4,2,9])
y4 = np.array([10,30,40,60])
plt.subplot(2,2,4)
plt.plot(x4,y4,marker = '.',color = "pink",ls = 'solid')
plt.show()