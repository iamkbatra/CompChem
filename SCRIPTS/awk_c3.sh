#!/bin/bash
cat test1br.xyz | tail -169 | head -166 | awk '{printf "%-s\t %8.5f\t %8.5f\t %8.5f \n",  $1, $2/23.5, $3/23.5, $4/6.5}' > output.dat
