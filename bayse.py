#Bayse
import matplotlib.pyplot as plt
import math

evidence = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1] #0が表、1が裏
probability = [0.2, 0.2, 0.2, 0.2, 0.2] #各仮説の事前確率0.1から0.5まで0.1刻み
xdata = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
hypo = [[0]*len(evidence) for i in range(len(probability))]

def bayse(evidence, probability):
     under = 0
     for i in range(len(probability)):
          if(evidence == 0):
               under += probability[i] * (0.1 + 0.1*i)
          else:
               under += probability[i] * (1-(0.1 + 0.1*i))
     for i in range(len(probability)):
          upper = probability[i] * (0.1 + 0.1*i)
          probability[i] = upper / under
     
     return probability

#main
for i in range(len(evidence)):
     probability = bayse(evidence[i], probability)
     for j in range(len(hypo)):
          hypo[j][i] = probability[j]

for i in range(len(hypo)):
     plt.plot(xdata, hypo[i])
     number = math.floor((0.1 + 0.1*i)*10)/10
     plt.title("Hypothesis "+str(number))
     plt.xlabel("time")
     plt.ylabel("probability")
     plt.savefig("Hypothesis"+str(i+1)+".png")
     plt.cla()
     plt.clf()
"""
print(hypo[4])
plt.plot(xdata, hypo[4])
plt.show()
"""
print("Results")
for i in range(len(probability)):
     print(str(0.1+0.1*i)+": "+str(probability[i]))
