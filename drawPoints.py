import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y = [1,2,4,3,4,5,6,4,8,7,12,11,11,8,5,6,7,10,6,4]

xMin = []
yMin = []

for z in range (0, len(y)):
    if y[z] == min(y):
        xMin.append(x[z])
        yMin.append(y[z])

maxX = max(x)
maxY = max(y)
minX = min(x)
minY = min(y)

plt.plot(x, y, marker = 'o', linestyle = '-')
plt.plot(xMin, yMin, linewidth = 4, linestyle = '-')
plt.axis([(minX - 1), (maxX + 1), (minY - 1), (maxY + 1)])

print ("this is plot demo")
plt.show()
