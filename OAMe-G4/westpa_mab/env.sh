#!/bin/sh
#
# env.sh
#
# This script defines environment variables that are used by other shell
# scripts, both when setting up the simulation and when running the simulation.
#

source /home/dray@iit.local/gromacs-2021.5/install_single_cuda/bin/GMXRC

export WEST_SIM_ROOT="$PWD"
export SIM_NAME=$(basename $WEST_SIM_ROOT)

