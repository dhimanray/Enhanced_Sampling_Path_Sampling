import numpy as np

l = np.loadtxt('COLVAR')

for i in range(len(l)):
    print("%0.4f"%(2.0-l[i,1])) #increasing
