import numpy as np
import os

ss = np.loadtxt('successful.txt')

weights = ss[:,2]

arr = weights.copy()

#largest 10 weights index
indices = arr.argsort()[-10:][::-1]

for i in indices:
    namelist = []
    #trace the path of each successful transition to the beginning
    os.system('w_trace %d:%d'%(ss[i,0],ss[i,1]))
    os.system('rm trajs.h5')

    #merge the xtc files along traced path
    l = np.loadtxt('traj_%d_%d_trace.txt'%(ss[i,0],ss[i,1]))
    for j in range(1,len(l)):
        fname = 'traj_segs/%06d/%06d/traj_comp.xtc'%(l[j,0],l[j,1])
        namelist.append(fname)
    namestring = ' '.join(namelist)
    os.system('gmx_mpi trjcat -f %s -o merged_trajectories/trace_%d_%d.xtc -cat'%(namestring,ss[i,0],ss[i,1])) 
    #print(namestring)



