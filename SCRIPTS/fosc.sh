#!/bin/bash

grep -A7 "ELECTRIC DIPOLE" output | sed -n -e '6,$p' | awk '{printf "%.9f,", $4}END{print ""}'
