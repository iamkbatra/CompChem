#!/bin/bash
#PBS -l nodes=1:ppn=20
#PBS -q dque
#PBS -r n
#PBS -m e
#PBS -j oe
#PBS -l walltime=99999:00:00
#PBS -N MIL125TINH2_OPT2

cd $PBS_O_WORKDIR

source  /opt/intel/oneapi/setvars.sh  --force

/opt/intel/oneapi/mpi/2021.1.1/bin/mpirun -n 20  /opt/VASP/INTELONE/vasp_std  > vasp.log 2>&1
