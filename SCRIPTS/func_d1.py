import pandas
import matplotlib.pyplot as plt
import seaborn as sns

fulldata = pandas.read_csv("DFT_Functionals.csv", index_col="Source").T
functionals= fulldata[[column for column in fulldata.columns if column!="Experimental"]].astype(float)
experimental =  fulldata["Experimental"].astype(float)
for f in functionals:
    error = (functionals[f]-experimental)/experimental
    scaling = 1.0 - error.mean()
 
    print "functional "+f+"scaling factor = ", scaling
    functionals[f] *= scaling

print(functionals)

