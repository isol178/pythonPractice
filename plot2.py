import matplotlib.pyplot as plt
import math

T = 5
C = 10
F = 100
r = 0.12
t = 0  #tの初期値
dt = 0.1
digits = - math.log10(dt)
steps = int(T/dt)
xdata = []
ydata = []

def preValue(t):
    payStep = int(T - math.floor(t))
    preValue = 0
    x = T - t
    if(x != 0):
        for i in range(payStep):
            #print(x)
            if(i > 0):
                preValue = preValue + C * math.exp(-x*r)
                #print(-x*r)
            else:
                preValue = preValue + (C + F)*math.exp(-x*r)
            x = x - 1
    else:
        preValue = C + F
    return preValue

#print(preValue(4.5))

for i in range(steps):
    xdata.append(t)
    #print(t)
    ydata.append(preValue(t))
    #print(t, dt)
    t = t + dt
    t = math.ceil(t*(10**digits))/(10**digits)
    if(t > T):
        break

#print(xdata)
#print(ydata)
plt.plot(xdata,ydata)
plt.title("Present Value of bond")
plt.xlabel("t")
plt.ylabel("V(t)")
plt.show()

