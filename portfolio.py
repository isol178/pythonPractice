import math
import numpy as np

ACC = 35.64
LAZ = 29.32
UFS = 20.99
ABBV = 94.91
WFC = 24.26
ETN = 93.13

ACC_r = 5.21
LAZ_r = 6.79
UFS_r = 8.36
ABBV_r = 4.91
WFC_r = 1.62
ETN_r = 3.09

fxRate = 105.76 #yen/dollar
budget = 60000 #yen

#等分配で考える
dollar = budget / fxRate
each = dollar // 6
stockPrice = [ACC, LAZ, UFS, ABBV, WFC, ETN]
stockReturn = [ACC_r, LAZ_r, UFS_r, ABBV_r, WFC_r, ETN_r]
quantity = [0, 0, 0, 0, 0, 0]
for p in range(len(stockPrice)):
     if(stockPrice[p] > each):
          quantity[p] = 1
     else:
          quantity[p] = each // stockPrice[p]
quantity[0] += 1.0
quantity[4] += 1.0
print(quantity)

requiredCash = 0
rtn = 0
stock = [0, 0, 0, 0, 0, 0]
for i in range(len(quantity)):
     requiredCash += quantity[i] * stockPrice[i]
     rtn += quantity[i] * stockPrice[i] * (stockReturn[i]/100)
     stock[i] = quantity[i] * stockPrice[i]
print(stock)
print("total = "+str(requiredCash)+" dollars")
print("In Yen, it's "+str(requiredCash*fxRate)+" yen")
print("expecting "+str(rtn)+" dollars = "+str(math.ceil(rtn*fxRate))+" yen as return")
