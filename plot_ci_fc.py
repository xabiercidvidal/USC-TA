import ROOT
import numpy as np
from matplotlib import pyplot as plt

## iterate in nobs, leave nbkg fixed
def get_ci(cl,nobs,nbkg):
    fc = ROOT.TFeldmanCousins(cl)
    o1,o2 = [],[]
    for nobsi in nobs:
        o1.append(fc.CalculateLowerLimit(nobsi,nbkg))
        o2.append(fc.CalculateUpperLimit(nobsi,nbkg))
    return np.array(o1),np.array(o2)


import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 20)

# Define different y ranges for the four subplots
nbkgs = [1,3,6,9]
y68min,y68max = {},{}
y90min,y90max = {},{}
for nbkg in nbkgs:
    y68min[nbkg],y68max[nbkg] = get_ci(0.68,x,nbkg)
    y90min[nbkg],y90max[nbkg] = get_ci(0.90,x,nbkg)


# Create a figure with a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(13, 8))
for i,ax in enumerate(axs.flat):
    nbkg = nbkgs[i]
    ax.fill_between(x, y90min[nbkg],y90max[nbkg], color='cornflowerblue', alpha=1,label='CL=90%')
    ax.fill_between(x, y68min[nbkg],y68max[nbkg], color='blue', alpha=1,label='CL=68%')
    ax.legend()
    ax.set_title("nbkg = {}".format(nbkg))
    ax.set_xlabel("nobs")
    ax.set_ylabel(r"$\mu$")


# Adjust layout
plt.tight_layout()
plt.show(block=False)
plt.savefig("figs/cl_intervals.png")
