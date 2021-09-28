#!/bin/bash
tail -n+25 "test10.cif" | awk '{ print $8 "\t" $3 "\t" $4 "\t" $5 }' > output.dat
