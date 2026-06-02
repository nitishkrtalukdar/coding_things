import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x=["Delhi","Mumbai","Chennai","Kolkata"]
y1=[10,12,8,11]
y2=[20,24,5,20]

plt.plot(x,y1,linestyle='-',color='purple',marker='o',markersize=6,label='condoms sold on 10th')
plt.plot(x,y2,linestyle='-.',color='red',marker='*',markersize=5,label='condoms sold on 14th')

plt.xlabel("Cities",fontsize=10,color='maroon')
plt.ylabel("Condoms Sold",fontsize=10,color='blue')
plt.title("Condom sold per city",fontsize=15,color='black')
plt.legend()
plt.show()