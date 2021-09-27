import pandas
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

fulldata = pandas.read_csv("DFT_Functionals.csv", index_col="Source").T
functionals= fulldata[[column for column in fulldata.columns if column!="Experimental"]].astype(float)
experimental =  fulldata["Experimental"].astype(float)

errors = pandas.DataFrame(index=functionals.index,columns=functionals.columns)
for f in functionals:
    # for functional f, scale the data 
    scaling = (experimental/functionals[f]).mean()
    functionals[f] *= scaling
    # calculate the error on all the structures with scaled values
    new_error = abs(functionals[f]-experimental)/experimental
    # store it in errors
    errors.loc[:,f] = new_error

# format and add mean error
metal = ["MgOEP","ZnOEP","MgTPP","ZnTPP","ZnTCPP","F-ZnP","DA-ZnP"]
org   = ["H2P","H2P.1","H2OEP","H2OEP.1","H2TPP","H2TPP.1","H2TAPP","H2TAPP.1"]

GGA_and_meta_GGA = ["PBE-D3-TDA(def2-SVP)","PBE-D3-RPA(def2-SVP)","PBE-D3-sTDA(def2-SVP)", "PBE-D3-sTDDFT(def2-SVP)", "PBE-D3-sTDA(def2-TZVP)","PBE-D3-sTDDFT (def2-TZVP)", "BP86-D3-TDA(def2-SVP)","BP86-D3-RPA(def2-SVP)","BP86-D3-sTDA(def2-SVP)","BP86-D3-sTDDFT(def2-SVP)","BP86-D3-sTDA(def2-TZVP)","BP86-D3-sTDDFT (def2-TZVP)","BLYP-D3-TDA(def2-SVP)","BLYP-D3-RPA(def2-SVP)","BLYP-D3-sTDA(def2-SVP)","BLYP-D3-sTDDFT(def2-SVP)","BLYP-D3-sTDA(def2-TZVP)","BLYP-D3-sTDDFT(def2-TZVP)","TPSS-D3-TDA(def2-SVP)","TPSS-D3-RPA(def2-SVP)","TPSS-D3-sTDA(def2-SVP)","TPSS-D3-sTDDFT(def2-SVP)","TPSS-D3-sTDA(def2-TZVP)","TPSS-D3-sTDDFT(def2-TZVP)","M06L-D3-TDA(def2-SVP)","M06L-D3-RPA(def2-SVP)","M06L-D3-sTDA(def2-SVP)","M06L-D3-sTDDFT(def2-SVP)","M06L-D3-sTDA(def2-TZVP)","M06L-D3-sTDDFT(def2-TZVP)"]

Hybrids = ["PBE0-D3-TDA(def2-SVP)","PBE0-D3-RPA(def2-SVP)","PBE0-D3-sTDA(def2-SVP)","PBE0-D3-sTDDFT(def2-SVP)","PBE0-D3-sTDA(def2-TZVP)","PBE0-D3-sTDDFT (def2-TZVP)","B3P-D3-TDA(def2-SVP)","B3P-D3-RPA(def2-SVP)","B3P-D3-sTDA(def2-SVP)","B3P-D3-sTDDFT(def2-SVP)","B3P-D3-sTDA(def2-TZVP)","B3P-D3-sTDDFT (def2-TZVP)","B3LYP-D3-TDA(def2-SVP)","B3LYP-D3-RPA(def2-SVP)","B3LYP-D3-sTDA(def2-SVP)","B3LYP-D3-sTDDFT(def2-SVP)","B3LYP-D3-sTDA(def2-TZVP)","B3LYP-D3-sTDDFT(def2-TZVP)","BHLYP-D3-TDA(def2-SVP)","BHLYP-D3-RPA(def2-SVP)","BHLYP-D3-sTDA(def2-SVP)","BHLYP-D3-sTDDFT(def2-SVP)","BHLYP-D3-sTDA(def2-TZVP)","BHLYP-D3-sTDDFT(def2-TZVP)","TPSS0-D3-TDA(def2-SVP)","TPSS0-D3-RPA(def2-SVP)","TPSS0-D3-sTDA(def2-SVP)","TPSS0-D3-sTDDFT(def2-SVP)","TPSS0-D3-sTDA(def2-TZVP)","TPSS0-D3-sTDDFT(def2-TZVP)","M06-D3-TDA(def2-SVP)","M06-D3-RPA(def2-SVP)","M06-D3-sTDA(def2-SVP)","M06-D3-sTDDFT(def2-SVP)","M06-D3-sTDA(def2-TZVP)","M06-D3-sTDDFT(def2-TZVP)","M062X-D3-TDA(def2-SVP)","M062X-D3-RPA(def2-SVP)","M062X-D3-sTDA(def2-SVP)","M062X-D3-sTDDFT(def2-SVP)","M062X-D3-sTDA(def2-TZVP)","M062X-D3-sTDDFT(def2-TZVP)"]

Range_Separated_Hybrids = ["CAM-B3LYP-D3-TDA(def2-SVP)","CAM-B3LYP-RPA(def2-SVP)","CAM-B3LYP-sTDA(def2-SVP)","CAM-B3LYP-sTDDFT(def2-SVP)","CAM-B3LYP-sTDA(def2-TZVP)","CAM-B3LYP-sTDDFT(def2-TZVP)","LC-BLYP-D3-TDA(def2-SVP)","LC-BLYP-D3-RPA(def2-SVP)","LC-BLYP-sTDA(def2-SVP)","LC-BLYP-D3-sTDDFT(def2-SVP)","LC-BLYP-D3-sTDA(def2-TZVP)","LC-BLYP-D3-sTDDFT(def2-TZVP)","wB97-D3-TDA(def2-SVP)","wB97-D3-RPA(def2-SVP)","wB97-D3-sTDA(def2-SVP)","wB97-D3-sTDDFT(def2-SVP)","wB97-D3-sTDA(def2-TZVP)","wB97-D3-sTDDFT(def2-TZVP)","wB97X-D3-TDA(def2-SVP)","wB97X-D3-RPA(def2-SVP)","wB97X-D3-sTDA(def2-SVP)","wB97X-D3-sTDDFT(def2-SVP)","wB97X-D3-sTDA(def2-TZVP)","wB97X-D3-sTDDFT(def2-TZVP)"]

Double_Hybrids_and_HF = ["B2PLYP(def2-SVP)","B2GP-PLYP(def2-SVP)","mPW2PLYP(def2-SVP)","CIS(def2-SVP)","CISD(def2-SVP)"]

errors = errors.T.pow(2.0)
errors["Mean"] = errors.mean(axis=1)
errors["Mean Metals"] = errors[metal].mean(axis=1)
errors["Mean Organic"] = errors[org].mean(axis=1)

col_to_type = {"GGA_and_meta_GGA":GGA_and_meta_GGA,
               "Hybrids":Hybrids,
               "Range_Separated_Hybrids":Range_Separated_Hybrids,
               "Double_Hybrids_and_HF":Double_Hybrids_and_HF}

for func_type, func_idx in col_to_type.iteritems():
    for ii in func_idx:
        errors.loc[ii,"FunctionalType"] = func_type

errors = errors.dropna()
errors = errors.reset_index()
errors = errors.set_index(["FunctionalType","Source"])

#make the grid

x_vars = ["Mean Organic","Mean Metals","Mean"]
y_vars = ["Source"]

errors = errors.loc[errors[x_vars].groupby(level=0)["Mean"].nsmallest(3).index, x_vars]
print(errors)
# errors = errors.sort_values(["FunctionalType","Mean"]).set_index(["FunctionalType","Source"])
errors.plot(rot=90)
plt.show()
raise

max_x = errors[x_vars].max().max()*1.1
min_x = errors[x_vars].min().min()*1.1
print(max_x)
y_vars = ["Source"] 
g = sns.PairGrid(errors, x_vars=x_vars, y_vars=y_vars)

# Draw a dot plot using the stripplot function
g.map(sns.stripplot,  orient="h", palette="Reds", edgecolor="gray")

g.set(xlim=(0, max_x), xlabel="Mean squared error", ylabel="")

for ax, title in zip(g.axes.flat, x_vars):
    # Set a different title for each axes
    ax.set(title=title)
    # Make the grid horizontal instead of vertical
    ax.xaxis.grid(False)
    ax.yaxis.grid(True)
plt.subplots_adjust(0.3,0.1,0.9,0.9)
sns.despine(left=True, bottom=True)


plt.show()
