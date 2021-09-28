#!/usr/bin/python3

import pandas as pd
import matplotlib as plt

fulldata = pd.read_csv("DFT_Functionals.csv", index_col="Source")

print(fulldata)
