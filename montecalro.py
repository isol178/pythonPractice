import random

trial = 50000
mu = 0
sigma = 1

sigma1 = 0
sigma2 = 0
sigma3 = 0

for i in range(trial):
    no = random.normalvariate(mu, sigma)
    if(no >= mu - sigma and no <= mu + sigma):
        sigma1 += 1
    if(no >= mu - 2*sigma and no <= mu + 2*sigma):
        sigma2 += 1
    if(no >= mu - 3*sigma and no <= mu + 3*sigma):
        sigma3 += 1
        
print("trials: "+str(trial)+"times Result: 1Sigma = "+str(sigma1/trial)+" 2Sigma = "+str(sigma2/trial)+" 3Sigma = "+str(sigma3/trial))
