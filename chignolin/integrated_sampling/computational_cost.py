import numpy as np
import os

os.system('grep "segments remain in iteration" west.log | cut -c1-2 > tmp')

l = np.loadtxt('tmp')

seg_length = 10 #in ps

for i in range(len(l)):
    print('Iteration: %d Computational cost: %d ps'%(i+1,int(seg_length*np.sum(l[:i]))))

os.system('rm tmp')
