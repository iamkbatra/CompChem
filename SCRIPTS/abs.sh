#!/bin/bash
awk '{ printf "%.5f \t %.5f \t %.5f \t %.5f \n", 1e7/$1, $2, $3, $4 }' orca.out.abs.dat > output.dat
