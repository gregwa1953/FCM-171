import plotext as plt
y1 = plt.sin(1000, 3)
y2 = plt.sin(1000, 3, 1.5, phase = 1)
plt.plot(y1, label = "plot")
plt.scatter(y2, label = "scatter", marker = "small")
plt.plotsize(100, 30)
plt.title("Multiple Data Set")
plt.show()

