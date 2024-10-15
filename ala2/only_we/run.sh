#!/bin/bash
#
# run.sh
#
# Run the weighted ensemble simulation. Make sure you ran init.sh first!
#

source env.sh

rm -f west.log
w_run --work-manager=threads --n-workers=8 "$@" &> west.log
