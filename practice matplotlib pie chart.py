import matplotlib.pyplot as plt
import numpy as np

# plt.pie(sales,labels=region)
# f=plt.figure()
# a=plt.axes(projection='3d')
# plt.show()

# f=plt.figure()
# an=plt.axes(projection='3d')
# z=np.linspace(0,10.1000)                   #3D
# x=np.sin(2*np.pi*z)
# y=np.cos(2*np.pi*z)
# x=z*np.sin(25*z)
# y=z*np.cos(25*z)
# a=an.plot3D(x,y,z,'green')


# f=plt.figure()
# an=plt.axes(projection='3d')
# z=np.linspace(0,10.1000)                   #Scatter plot
# # x=np.sin(2*np.pi*z)
# # y=np.cos(2*np.pi*z)
# x=z*np.sin(25*z)
# y=z*np.cos(25*z)
# a=an.scatter(x,y,z,'green')
# plt.show()



# data = np.random.normal(0, 1, 500)
# plt.figure(figsize=(6,4))
# plt.hist(data, bins=20, color='skyblue', edgecolor='black')
# plt.title("Basic Histogram")
# plt.xlabel("Value")                        #basic histogram
# plt.ylabel("Frequency")
# plt.show()


#histogram with custom watermark
data = np.random.normal(0, 1, 500)
plt.figure(figsize=(6,4))
plt.hist(data, bins=20, color='lightgreen', edgecolor='black')

# Add watermark
plt.text(0.5, 0.5, "Ramyaa", fontsize=40, color="gray",
         ha='center', va='center', alpha=0.25, rotation=30,
         transform=plt.gca().transAxes)
plt.title("Histogram With Watermark")
plt.show()

#Multiple histograms

data1 = np.random.normal(0, 1, 500)
data2 = np.random.normal(2, 1, 500)

plt.figure(figsize=(6,4))
plt.hist(data1, bins=20, alpha=0.5, label='Data 1')
plt.hist(data2, bins=20, alpha=0.5, label='Data 2')
plt.legend()
plt.title("Multiple Overlapping Histograms")
plt.show()


#2D histogram Heatmap

x = np.random.normal(0, 1, 5000)
y = np.random.normal(0, 1, 5000)

plt.figure(figsize=(6,5))
plt.hist2d(x, y, bins=40, cmap='viridis')
plt.colorbar(label='Count')
plt.title("2D Histogram")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

#Histogram with custom x-bins

data = np.random.normal(10, 3, 500)

# Custom bins
xbins = [0, 5, 8, 10, 12, 15, 20]

plt.figure(figsize=(6,4))
plt.hist(data, bins=xbins, edgecolor='black', color='cyan')
plt.title("Histogram with Custom X-Bins")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

#Scatter plot

x = np.random.rand(100)
y = x * 2 + np.random.normal(0, 0.1, 100)

plt.figure(figsize=(6,4))
plt.scatter(x, y, color='red')
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
