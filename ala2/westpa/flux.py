#calculating flux from the rescaled time data
import numpy as np
import matplotlib.pyplot as plt

l = np.loadtxt('time_data.txt')

flux = []
for i in range(1,len(l)):
    sum_weight = np.sum(l[0:i,2])
    max_time = np.max(l[0:i,1])
    flux.append(sum_weight/max_time)
#plt.yscale('log')
#plt.plot(l[1:,0],flux)
#plt.show()

f1 = open('flux_data.txt','w')
print('#count #flux #mfpt',file=f1)
for i in range(len(flux)):
    print(i+1,flux[i],1.0/flux[i],file=f1)
f1.close()
