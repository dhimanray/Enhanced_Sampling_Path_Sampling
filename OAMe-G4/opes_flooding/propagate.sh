#!/bin/bash

source source_gromacs_cuda.sh

export OMP_NUM_THREADS=1

for i in {16..30}
do
	cp -r template run$i
	cd run$i
	gmx_mpi grompp -f NVT.mdp -c b.gro -p topol.top -o prd.tpr
	mpiexec -n 1 gmx_mpi mdrun -deffnm prd -nsteps 100000000 -plumed plumed.dat -pin on -pinoffset 0
	cd ..
done
