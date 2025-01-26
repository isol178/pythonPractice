import numpy as np
import math

A = np.matrix([[5, 2, 1],[2, 1, 4],[1, 4, 2]])
b = np.matrix([[17],[11],[16]])
x = np.matrix([[0],[0],[0]])
epsilon = 1.0 * math.pow(10, -5)

r0 = b - A.dot(x)
p = r0
count = 0

while count < 100:
     alpha = r0.T.dot(r0)/p.T.dot(A.dot(p))
     alpha = alpha[0,0]
     x = x + alpha*p
     r1 = r0 - alpha*A.dot(p)
     # print(alpha*A.dot(p))
     # print("===============")
     print(x.T)
     count += 1
     if np.linalg.norm(r1) <= epsilon:
          print("finish")
          break
     beta = np.dot(r1.T, r1)/np.dot(r0.T, r0)
     beta = beta[0,0]
     p = r1 + beta*p
     r0 = r1
     # print(np.linalg.norm(r0))
     

print("trials: "+str(count))