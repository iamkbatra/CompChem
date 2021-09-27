awk '{printf "%s\t %.5f\t %.5f\t %.5f\n", $2, $3/23.5, $4/23.5, $5/6.22}' test.dat
