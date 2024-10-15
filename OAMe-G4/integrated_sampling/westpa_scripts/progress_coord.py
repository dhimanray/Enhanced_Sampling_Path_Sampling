import numpy as np

l = np.loadtxt('COLVAR')

for i in range(len(l)):
    print("%0.4f"%l[i,1]) 
