#!/bin/bash
#PBS -l nodes=1:ppn=10
#PBS -q dque
#PBS -r n
#PBS -m e
#PBS -j oe
#PBS -N GEO_OPT_PCE


cd $PBS_O_WORKDIR

/usr/local/openmpi-4.0.1/bin/mpirun -n 10  /opt/CP2K/cp2k-6.1-openmpi4-0-1/cp2k.psmp  -i Input-GEO_OPT.inp > Output-GEO_OPT.out
