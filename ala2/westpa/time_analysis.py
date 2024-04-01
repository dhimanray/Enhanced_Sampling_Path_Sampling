import numpy as np
import os

#================= PARAMETERS ==============================

barrier = 20 #from plumed.dat input file for OPES

T = 300 #Temperature in K

biasColumn = 3 #Column in which the bias is printed in the COLVAR file

dt = 0.1 #The frequency at which colvars is deposited (in ps)

time_unit = 10**12 #in ps

kT = 0.008273338*T #in kJ/mol

#===========================================================

#print all successful transitions
os.system('w_succ > successful.txt')
ss = np.loadtxt('successful.txt')

#open some files and folders
os.system('mkdir traces')
f1 = open('time_data.txt','w')
print('#Transition #Time (s) #weight from WE',file=f1) 

for j in range(len(ss)):
    #trace the path of each successful transition to the beginning
    os.system('w_trace %d:%d'%(ss[j,0],ss[j,1]))
    os.system('rm trajs.h5')

    #merge the COLVAR files along the traced path. In this way the
    #bias information is not necessary to store in progress coord
    l = np.loadtxt('traj_%d_%d_trace.txt'%(ss[j,0],ss[j,1]))
    os.system('rm trace_%d_%d'%(ss[j,0],ss[j,1]))
    os.system('touch trace_%d_%d'%(ss[j,0],ss[j,1]))
    for i in range(1,len(l)):
        fname = 'traj_segs/%06d/%06d/COLVAR'%(l[i,0],l[i,1])
        os.system('cat %s >> trace_%d_%d'%(fname,ss[j,0],ss[j,1]))

    #load COLVAR file and rescale time
    cv = np.loadtxt('trace_%d_%d'%(ss[j,0],ss[j,1]))

    c = 0
    for i in range(len(cv)):
        b = np.exp((cv[i,biasColumn-1]+barrier)/kT)
        c += dt*b

    rescaled_time = c/time_unit
    weight = ss[j,2] 

    print(j+1,rescaled_time,weight,file=f1)

    #move unnecessary trace files to the traces folder
    os.system('mv traj_%d_%d_trace.txt traces/'%(ss[j,0],ss[j,1]))
    os.system('mv trace_%d_%d traces/'%(ss[j,0],ss[j,1]))

f1.close()
