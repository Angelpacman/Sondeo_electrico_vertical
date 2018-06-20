"""
este programa grafica las resistividades
aparentes
a partir de un archivo .csv
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos = pd.read_csv('sev_KR02.csv')

"""
AB/2 esta representado por AB y MN/2 ESTA DECLARADA por MN
"""

AB = datos.iloc[:,0]
MN = datos.iloc[:,1]
I  = datos.iloc[:,2]
V  = datos.iloc[:,3]

KG = np.pi*((AB-MN)*(AB+MN))/(2*MN)

Rhoa = KG*V/I

#print(datos)

print('\n')
print(Rhoa)

with plt.style.context(('classic')):

    plt.plot(AB,Rhoa)
    plt.semilogy(AB,Rhoa)
    plt.grid(True, which = 'both')
    plt.scatter(AB,Rhoa)

    plt.yscale("log")
    plt.xscale('log')

    plt.ylim([1,1000])
    plt.xlim([1,1000])

    plt.xlabel('AB/2')
    plt.ylabel('Resistividad aparente')
    plt.title('Sondeo Electrico Vertical KR02')

    #plt.setp(AB, Rhoa, rotation=45, horizontalalignment='right')
plt.show()
