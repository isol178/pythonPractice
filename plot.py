import matplotlib.pyplot as plt

u = 0.2
r = 0.1
dd = 0.01
steps = int((min(r, u) + 1)/dd)
xdata = []
ydata = []
d = -1

for i in range(steps - 1):
    d = d + dd
    #print(d)
    xdata.append(d)
    ydata.append((r - d)/(u - d))

for i in range(steps):
    plt.plot(xdata,ydata)

plt.title("Risk Neutral Probability")
plt.xlabel("d")
plt.ylabel("p*")
plt.show()
