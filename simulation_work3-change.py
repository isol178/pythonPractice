import numpy as np
import matplotlib.pyplot as plt
import math

#計算領域の大きさ(単位：m)
width = 0.1
height = 0.1

#格子の大きさ 一辺0.005mの正方格子
Nx = 19
Ny = 19
cordA = 85 #点Aの座標は(10,5) 通し番号は 4*19+9

#境界条件: 断熱条件

#使用変数
N = Nx*Ny
dx = width / (Nx + 1)
dy = height / (Ny + 1)
a1 = -2.0/dx/dx - 2.0/dx/dx
a2 = 1.0/dx/dx
a4 = 1.0/dy/dy
dt = 0.05
timesteps = 500
it_out = [k for k in range(1, timesteps, int(timesteps/10))]
#物性値等
thermalCoductivity = 399  #equals to lambda
Cp = 385 * 8960
eta = 2 * math.pow(10, -8) #電気抵抗率
d = 0.01 #板の厚さ(m)
#外部磁場の情報
B = 1.2
f = 100

pi = math.pi
JJ = np.zeros((N, 1))        #NumPyの行列は左上が始点であることに注意
P = np.zeros((N, N))
P_iso = np.zeros((N, N))
P2 = np.zeros((N, N))
mu0 = 4 * pi * math.pow(10, -7)   #真空の透磁率
T = np.zeros((Ny+2, Nx+2))
M_new = np.zeros((N, 1))
T_new = np.zeros((N, 1))
Temp = np.zeros((timesteps, 1))
JxREC = np.zeros((timesteps, 1))

#プロットを行う
def plotTemperatures(T, time):
    X = np.arange(0,Nx)
    Y = np.arange(0,Ny)
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

#Rの計算関数
def calcR(time):
    R = np.zeros((N, 1)) + (2*B*pi*f*math.sin(2*pi*f*time))
    return R

#境界の様子の設定
def boundary(T):
    for j in range(Ny+2):
        for i in range(Nx+2):
            if(i == 0):
                if(j != 0 and j != Ny+1):
                    T[i, j] = T[i+1, j]
                elif(j == 0):
                    T[i, j] = T[i+1, j+1]
                else:
                    T[i, j] = T[i+1, j-1]
            elif(i == Nx+1):
                if(j != 0 and j != Ny+1):
                    T[i, j] = T[i-1, j]
                elif(j == 0):
                    T[i, j] = T[i-1, j+1]
                else:
                    T[i, j] = T[i-1, j-1]
            elif(j == 0):
                if(i != 0 and i != Nx+1):
                    T[i, j] = T[i, j+1]
            elif(j == Ny+1):
                if(i != 0 and i != Nx+1):
                    T[i, j] = T[i, j-1]

#P_iso,P,P2の計算
for j in range(1, Ny+1):
    for i in range(1, Nx+1):
        alpha = (j-1)*Nx + (i-1)
        P[(alpha, alpha)] = a1
        P_iso[(alpha, alpha)] = a1
        if(i > 1):
            P[alpha, alpha-1] = a2
            P_iso[alpha, alpha-1] = a2
        else:
            P_iso[alpha, alpha] += a2
        
        if(i < Nx):
            P[alpha, alpha+1] = a2
            P_iso[alpha, alpha+1] = a2
        else:
            P_iso[alpha, alpha] += a2
        
        if(j > 1):
            P[alpha, alpha - Nx] = a4
            P_iso[alpha, alpha - Nx] = a4
        else:
            P_iso[alpha, alpha] += a4
            
        if(j < Ny):
            P[alpha, alpha + Nx] = a4
            P_iso[alpha, alpha + Nx] = a4
        else:
            P_iso[alpha, alpha] += a4
        P2 = P.copy() * (- eta)

#Q2の計算
Q1 = np.eye(N) * mu0
Q2 = np.zeros((N, N))
for j2 in range(1, Ny+1):
    for i2 in range(1, Nx+1):
        for j1 in range(1, Ny+1):
            for i1 in range(1, Nx+1):
                alpha = (j1-1)*Nx + i1-1
                beta = (j2-1)*Ny + i2-1
                distance = math.sqrt((((i1-i2)**2)*(dx**2) + ((j1-j2)**2)*(dy**2) + (d/2)**2))
                Q2[alpha, beta] = - mu0*d*dx*dy /(4*pi*math.pow(distance,3))

#メインプロシージャ
k = 0
for it in range(1, timesteps):
    #solveMagneticEquation(it) 電磁誘導方程式を解く
    M_old = M_new.copy()
    Left = (Q1 + Q2)/dt + P2
    Right = ((Q1 + Q2)/dt)*M_old + calcR(it)
    M_new = np.dot(np.linalg.inv(Left), Right)
    #calcJ() Jの構造が合っているか自信がない
    for j in range(Ny):
        for i in range(Nx):
            alpha = (j-1)*Nx + (i-1)
            Jx = (M_new[alpha+Nx, 0] - M_new[alpha-Nx, 0])/(2*dy)
            Jy = - (M_new[alpha+1, 0] - M_new[alpha-1, j])/(2*dx)
            JJ[alpha, 0] = math.pow(Jx, 2) + math.pow(Jy, 2)
            if(alpha == cordA):
                JxREC[it, 0] = Jx
    #solveThermalEquation() 二次元熱伝導方程式を後退差分法で解く
    T_old = T_new.copy()
    I = np.eye(N)
    P3 = I - ((thermalCoductivity*dt)/Cp * P_iso)
    Right = T_old + ((dt*eta)/Cp * JJ)
    T_new = np.dot(np.linalg.inv(P3), Right)
    #recording
    Temp[it, 0] = T_new[cordA, 0]
    if(k < len(it_out) and it == it_out[k]):
                T = T_new.reshape(Ny, Nx)
                #boundary(T)
                plotTemperatures(T, it)
                k += 1

#csvファイル作成
np.savetxt("TemperatureAtPointA_Cu.csv", X = Temp, delimiter=",")
np.savetxt("JxAtPointA_Cu.csv", X = JxREC, delimiter=",")
