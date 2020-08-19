import numpy as np
import matplotlib.pyplot as plt
import math

#計算領域の大きさ(単位：m)
width = 0.1
height = 0.1

#格子の大きさ
Nx = 11
Ny = 11

#境界条件に使う温度
T1 = 0.0
T2 = 100.0

#使用変数
N = Nx*Ny
dx = width / (Nx + 1)
dy = height / (Ny + 1)
a1 = -2.0/dx/dx - 2.0/dx/dx
a2 = 1.0/dx/dx
a4 = 1.0/dy/dy
dt = 0.05
timesteps = 200
it_out = [k for k in range(1, timesteps, int(timesteps/10))]
#以下物性値
thermalCoductivity = 399
Cp = 385 * 8960

Psi = np.zeros((N, 1))         #NumPyの行列は左上が始点であることに注意
P = np.zeros((N, N))
T = np.zeros((Ny + 2, Nx + 2))

#境界条件の設定
def boundary(T):
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

#プロットを行う
def plotTemperatures(T, time):
    X = np.arange(0,Nx+2)
    Y = np.arange(0,Ny+2)
    plt.contourf(X, Y, T, levels = 10, cmap = "coolwarm")
    plt.colorbar()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Cu Temperature at "+str(math.floor(time*dt*100)/100)+"sec")
    file_title = "TempCu" + str(time) + ".png"
    plt.savefig(file_title)
    plt.cla()
    plt.clf()
    #plt.show()

boundary(T) #初期設定
T_first = T

#PとPsiの計算
for j in range(1, Ny+1):
    for i in range(1, Nx+1):
        alpha = (j-1)*Nx + (i-1)
        P[(alpha, alpha)] = a1
        if(i > 1):
            P[alpha, alpha-1] = a2
        else:
            Psi[alpha, 0] += - a2*T_first[0, j]
        
        if(i < Nx):
            P[alpha, alpha+1] = a2
        else:
            Psi[alpha, 0] += - a2*T_first[Nx+1, j]
        
        if(j > 1):
            P[alpha, alpha - Nx] = a4
        else:
            Psi[alpha, 0] += - a4*T_first[i, 0]
        
        if(j < Ny):
            P[alpha, alpha + Nx] = a4
        else:
            Psi[alpha, 0] += - a4*T_first[i, Ny+1]

#print(P)
#print(Psi)

#二次元熱伝導方程式を後退差分法で解く
I = np.eye(N)
invA = I * (- thermalCoductivity/Cp) 
Q = I + dt * np.dot(invA, P)
middle = int(N/2)
Temp = np.zeros((timesteps, 1))
k = 0
T_new = np.zeros((N, 1))
for it in range(1, timesteps):
    T_old = T_new.copy()
    T_new = np.dot(np.linalg.inv(Q), (T_old - (thermalCoductivity*dt/Cp * Psi)))
    Temp[it, 0] = T_new[middle, 0]
    if(k < len(it_out) and it == it_out[k]):
        T = np.zeros((Ny+2, Nx+2))
        boundary(T)
        T[1:Ny+1, 1:Nx+1] = T_new.reshape(Ny, Nx)
        plotTemperatures(T, it)
        k += 1

#csvファイル作成
#np.savetxt("TemperatureInTheMiddle_Au.csv", X = Temp, delimiter=",")
