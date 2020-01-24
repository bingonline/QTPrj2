# _*_ coding utf-8 _*_
#开发人员 bing
#开发日期 2020/1/24 14:59
#文件名称 LearnPlot.py
#开发工具 PyCharm

import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)
a=np.arange(0.0,5.0,0.02)
plt.subplot(211)
plt.plot(a,f(a))
plt.subplot(2,1,2)
plt.plot(a,np.cos(f(a)),'r--')
plt.show()
