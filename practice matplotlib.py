# import matplotlib.pyplot as plt
# x=[0,1,3,5,8]
# y=[2,4,6,7,9]
# # plt.plot(x,y,marker='o',linestyle='--',color='r')
# # plt.show() 
# figure, ax = plt.subplots()
# # ax.plot(x,y,marker='o')
# # plt.show()

# ax.plot(x,y,marker='o',label="Data points")
# ax.set_title("Sample title")
# ax.set_xlabel("X-axis")
# ax.set_ylabel("Y-axis")
# plt.legend()
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
# x=np.array([1,2,3,4,5])
# y=x*2
# plt.plot(x,y,marker='o',label="Data points")
# for i in range(0,len(x)):
#     plt.annotate('({0},{1})'.format(x[i],y[i]),xy=(x[i],y[i]),textcoords="offset points")
#     xy=(x[i],y[i])
# plt.show()  

# x=[1,2,3,4,5]
# y=[1,2,3,4,5]
# plt.plot(x,y)
# x=[2,3,4,5,]
# y=[1,2,3,4]
# plt.plot(x,y)
# plt.fill_between(x,y, color='blue', alpha=0.5)
# plt.show()

# x=['apple','banana','grape','orange']
# y=[10,15,7,12]
# plt.barh(x,y)
# x=[2,3,4,5,]
# y=[1,2,3,4]
# plt.barh(x,y)
# plt.fill_between(x,y, color='blue', alpha=0.5)
# plt.show()

# x=['apple','banana','grape','orange']
# y=[10,15,7,12]
# widths=[0.5]
# plt.barh(x,y)
# x=[2,3,4,5,]
# y=[1,2,3,4]
# widths=[0.5]
# plt.barh(x,y)
# plt.fill_between(x,y, color='blue', alpha=0.5)
# plt.show()   

# years=[2015,2016,2017,2018,2019]
# samsung=[50,55,60,65,70]
# vivo=[30,35,40,45,50]
# oppo=[20,25,30,35,40]
# plt.bar (years,samsung,color='r',label='samsung')



# years=[2015,2016,2017,2018,2019]
# samsung=[50,55,60,65,70]
# vivo=[30,35,40,45,50]
# oppo=[20,25,30,35,40]
# plt.bar (years,vivo,color='g',label='vivo')
# plt.xlabel('years')
# plt.ylabel('sales')
# plt.legend()
# plt.show()

years=[2015,2016,2017,2018,2019]
samsung=[50,55,60,65,70]
vivo=[30,35,40,45,50]
oppo=[20,25,30,35,40]
plt.bar ((0,1,2,3,4),vivo,color='g',label='vivo',width=0.25)
plt.bar((0.25,1.25,2.25,3.25,4.25),oppo,color='orange',label='oppo',width=0.25)
plt.bar((0.5,1.5,2.5,3.5,4.5),samsung,color='b',label='samsung',width=0.25)
# z=[i+0.2 for i in years]
plt.xlabel('years')
plt.ylabel('sales')
plt.legend()
plt.show()