import numpy as np
import matplotlib.pyplot as plt

#出力ファイル名
fp1 = "Pmat.csv"
fp2 = "Psi.csv"

#計算領域の大きさ(単位：m)
width = 0.1
height = 0.1

#格子の大きさ
Nx = 11
Ny = 11

#境界条件に使う温度
T1 = 0.0
T2 = 100.0

N = Nx*Ny
dx = width / (Nx + 1)
dy = height / (Ny + 1)
a1 = -2.0/dx/dx - 2.0/dx/dx
a2 = 1.0/dx/dx
a4 = 1.0/dy/dy

Psi = np.zeros((N, 1))         #NumPyの行列は左上が始点であることに注意
P = np.zeros((N, N))
T = np.zeros((Ny + 2, Nx + 2))

#境界条件の設定
for j in range(Ny+2):
    for i in range(Nx+2):
        if(i == 0 or j == 0):
            if(i != Nx+1 and j != Ny+1):
                T[i, j] = T1
            else:
                T[i, j] = (T1 + T2)/2
        if(i == Nx+1 or j == Ny+1):
            if(i != 0 and j != 0):
                T[i, j] = T2

for j in range(1, Ny+1):
    for i in range(1, Nx+1):
        alpha = (j-1)*Nx + (i-1)
        P[(alpha, alpha)] = a1
        if(i > 1):
            P[alpha, alpha-1] = a2
        else:
            Psi[alpha, 0] += - a2*T[0, j]
        
        if(i < Nx):
            P[alpha, alpha+1] = a2
        else:
            Psi[alpha, 0] += - a2*T[Nx+1, j]
        
        if(j > 1):
            P[alpha, alpha - Nx] = a4
        else:
            Psi[alpha, 0] += - a4*T[i, 0]
        
        if(j < Ny):
            P[alpha, alpha + Nx] = a4
        else:
            Psi[alpha, 0] += - a4*T[i, Ny+1]

#print(P)
#print(Psi)

#温度計算
T_vec = np.dot(np.linalg.inv(P), Psi)
for x in range(N):
    i = x // Nx
    j = x - i*Nx
    T[i+1, j+1] = T_vec[x, 0]
#T = T[::-1,:] #温度分布を問題に合わせた向きに調整
#print(T)

#csvファイル作成
#np.savetxt("Temperature.csv", X = T, delimiter=",")

#プロットを行う
X = np.arange(0,Nx+2)
Y = np.arange(0,Ny+2)
plt.contourf(X, Y, T, levels = 10, cmap = "coolwarm")
plt.colorbar()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Temperature")
plt.show()
