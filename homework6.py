import math

def cmb(n, r):
    answer = math.factorial(n) // math.factorial(r) // math.factorial(n-r)
    return answer

def fi(m, N, p):
    answer = 0
    for k in range(m+1):
        answer += cmb(N, k) * math.pow(p, k) * math.pow(1-p, N-k)
    return answer

m = 35
N = 50
p = 0.7537

print(fi(m-1, N, p))
