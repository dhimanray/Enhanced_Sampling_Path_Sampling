#!/bin/bash
export OMP_NUM_THREADS=1

for i in {3..30}
do
	cp -r template run$i
	cd run$i

	gmx_mpi grompp -f md.mdp -c config.gro -p topol.top -o input.tpr

	mpiexec -n 1 gmx_mpi mdrun -s input.tpr -deffnm alanine -plumed plumed.dat -nsteps 5000000 -pin on -pinoffset 34
	
	cd ..
done	
