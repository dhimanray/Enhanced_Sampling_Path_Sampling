import numpy as np

l = np.loadtxt('time_data.txt')

f1 = open('mfpt.dat','w')
sum_tw = 0.0
sum_w = 0.0

print('#Transition #Interation #MFPT(s)',file=f1)

for i in range(len(l)):
    sum_tw += l[i,4]*l[i,3]
    sum_w += l[i,4]
    print(l[i,0],l[i,1],sum_tw/sum_w,file=f1)
f1.close()
