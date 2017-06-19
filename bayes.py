import numpy as np
import matplotlib.pyplot as plt
import random

with open("dataA.txt", "r") as ins:
    dataA= []
    for line in ins:
        for word in line.split():
            dataA.append(word)

with open("dataB.txt", "r") as ins:
    dataB= []
    for line in ins:
        for word in line.split():
            dataB.append(word)

Ax = np.zeros(len(dataA)/2)
Ay = np.zeros(len(dataA)/2)
i = 0
l = 0
while i<len(dataA):
    Ax[l] = (float)(dataA[i])
    Ay[l] = (float)(dataA[i+1])
    i+=2
    l+=1

Bx = np.zeros(len(dataB) / 2)
By = np.zeros(len(dataB) / 2)
i = 0
l = 0
while i < len(dataB):
    Bx[l] = (float)(dataB[i])
    By[l] = (float)(dataB[i + 1])
    i += 2
    l += 1

allPoints = len(Ax) + len(Bx)

aprioriA = len(Ax)/allPoints
aprioriB = len(Bx)/allPoints

for j in range(10):
    ilosc = 0
    promien = 0.2
    newX = random.uniform(0,2.2)
    newY = random.uniform(1.8,6.2)
    while ilosc<6:
        szansaA = 0
        szansaB = 0

        for a in range(len(Ax)):
            if np.abs(Ax[a]-newX)<promien and np.abs(Ay[a]-newY)<promien and np.sqrt((np.abs(Ax[a]-newX))**2 + (np.abs(Ay[a]-newY))**2)<promien:
                szansaA+=1
        for a in range(len(Bx)):
            if np.abs(Bx[a]-newX)<promien and np.abs(By[a]-newY)<promien and np.sqrt((np.abs(Bx[a]-newX))**2 + (np.abs(By[a]-newY))**2)<promien:
                szansaB+=1
        promien += 0.1
        ilosc = szansaA + szansaB
    szansaA = szansaA/len(Ax)
    szansaB = szansaB / len(Bx)
    prawdA = szansaA*aprioriA
    prawdB = szansaB*aprioriB
    if prawdA>prawdB:
        plt.plot(newX,newY,'*r')
    else:
        plt.plot(newX, newY, 'xg')
    print(prawdA)
    print(prawdB)
plt.plot(Ax,Ay,'xr')
plt.plot(Bx,By,'*g')
plt.show()