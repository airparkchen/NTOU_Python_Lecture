#pip install matplotlib
#pip install numpy
import numpy as np
import matplotlib
import matplotlib.pyplot as plt	#匯入Pyplot 套件並命名為plt
#1
xpoints = np.array([0, 3])

ypoints = np.array([0, 150])

plt.plot(xpoints, ypoints)

plt.show()

#2
# xpoints = np.array([1, 5])

# ypoints = np.array([3, 7])

# plt.plot(xpoints, ypoints, 'o') 
#在圖中繪製兩個點，分別是(1,3)、（5,7）
#將點用’o’來做標記

# plt.show()

#3
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker = 'o')

# plt.show()

#4
# import matplotlib.pyplot as plt

# import numpy as np

# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, 'o:r') #格式是 標記 | 線 | 顏色

# plt.show()

#5
import matplotlib.pyplot as plt

import numpy as np

x1 = np.array([0, 1, 2, 3])

y1 = np.array([3, 8, 1, 10])

x2 = np.array([0, 1, 2, 3])

y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)

plt.show()

# #6
# import matplotlib.pyplot as plt

# import numpy as np

#plot 1:

x = np.array([0, 1, 2, 3])

y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)	#一行，兩列，第一個圖表

plt.plot(x,y)

#plot 2:

x = np.array([0, 1, 2, 3])

y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)	#一行，兩列，第二個圖表

plt.plot(x,y)

plt.show()