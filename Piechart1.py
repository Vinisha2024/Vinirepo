import numpy as np
from matplotlib import pyplot as plt
x = np.array([15,20,45,60,10])
lab = ['JAVA','JAVASCRIPT','PYTHON','C#','C++']
ex = (0,0,0.2,0.1,0)
plt.pie(x,labels = lab,explode = ex,autopct='%1.1f%%',hatch=['**O', 'oO', 'O.O', '.||.'],radius=1)
plt.legend(title = 'Languages',loc = 'center left')
plt.show()
