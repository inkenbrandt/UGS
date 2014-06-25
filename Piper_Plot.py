# -*- coding: utf-8 -*-
"""
Created on Thu May 29 10:57:49 2014

@author: paulinkenbrandt
"""

# -*- coding: utf-8 -*-
""" Hydrochemistry - Construct Rectangular Piper plot

    Adopted from: Ray and Mukherjee (2008) Groundwater 46(6): 893-896 
    Development date: 8/5/2011
    http://python.hydrology-amsterdam.nl/scripts/piper_rectangular.py

    - Prepare an input text file. Observations are expected have meq/l units with parameters in the order: Cl, HCO3, SO4, Na+K, Ca, Mg

    - Example input file. If observations are missing, label them as -9999:

    Type Cl HCO3 SO4 NaK Ca Mg EC NO3 Sicc
    1 1.72 4.02 0.58 1.40 4.53 0.79 672.00 0.40 0.21
    2 0.90 1.28 0.54 0.90 1.44 0.74 308.00 0.36 0.56
    2 4.09 4.29 0.38 3.38 4.74 0.72 884.00 0.08 0.15

    - Insert the correct file name and delimiter in the loadtxt() statement

    - Specify legend for figure

    - Run the script and look at the plot
    
"""

__author__ = "B.M. van Breukelen <b.m.vanbreukelen@vu.nl>"
__version__ = "1.0"
__date__ = "Nov 2012"


from pylab import * # the pylab module combines Pyplot (MATLAB type of plotting) with Numpy into a single namespace

# Specify locations of files and open the files
# -------------------------------------------------------------------------------- #
#
# Import observations
# Observations are expected have meq/l units with parameters in the order: Cl, HCO3, SO4, Na+K, Ca, Mg
obs=loadtxt('watersamples.txt', delimiter=' ', comments='#') # first row with headers is skipped, matrix with data is assigned to obs
obs[obs == -9999] = NaN # if observations are missing, label them as -9999 (for example) in excel and make them Not a Number (NaN)

nosamples = len(obs[:,0]) # Determine number of samples in file

# Column Index for parameters
Cl = 1
HCO3 = Cl+1
SO4 = Cl+2
NaK = Cl+3
Ca = Cl+4
Mg = Cl+5
EC = Cl+6

# Change default settings for figures
# -------------------------------------------------------------------------------- #
rc('savefig', dpi = 300)
rc('xtick', labelsize = 10)
rc('ytick', labelsize = 10)
rc('font', size = 12)
rc('legend', fontsize = 12)
rc('figure', figsize = (14,4.5)) # defines size of Figure window

markersize = 8
linewidth = 2
xtickpositions = linspace(0,100,6) # desired xtickpositions for graphs

# Make Figure
# -------------------------------------------------------------------------------- #

fig=figure()

# CATIONS
# 2 lines below needed to create 2nd y-axis (ax1b) for first subplot
ax1 = fig.add_subplot(131)
ax1b = ax1.twinx()

ax1.fill([100,0,100,100],[0,100,100,0],color = (0.8,0.8,0.8))
ax1.plot([100, 0],[0, 100],'k')
ax1.plot([50, 0, 50, 50],[0, 50, 50, 0],'k--')
ax1.text(25,15, 'Na type')
ax1.text(75,15, 'Ca type')
ax1.text(25,65, 'Mg type')

# loop to use different symbol marker for each water type
for i in range(0, nosamples):
    if obs[i, 0] > 0:
        ax1.plot(100*obs[i,Ca]/(obs[i,EC]/100), 100*obs[i,Mg]/(obs[i,EC]/100), 'ro', ms = markersize)
#    if obs[i, 0] == 2:
#        ax1.plot(100*obs[i,Ca]/(obs[i,EC]/100), 100*obs[i,Mg]/(obs[i,EC]/100), 'b>', ms = markersize)
#    if obs[i, 0] == 3:
#        ax1.plot(100*obs[i,Ca]/(obs[i,EC]/100), 100*obs[i,Mg]/(obs[i,EC]/100), 'c<', ms = markersize)
#    if obs[i, 0] == 4:
#        ax1.plot(100*obs[i,Ca]/(obs[i,EC]/100), 100*obs[i,Mg]/(obs[i,EC]/100), 'go', ms = markersize)
#    if obs[i, 0] == 5:
#        ax1.plot(100*obs[i,Ca]/(obs[i,EC]/100), 100*obs[i,Mg]/(obs[i,EC]/100), 'm^', ms = markersize)

ax1.set_xlim(0,100)
ax1.set_ylim(0,100)
ax1b.set_ylim(0,100)
ax1.set_xlabel('<= Ca (% meq)')
ax1b.set_ylabel('Mg (% meq) =>')
setp(ax1, yticklabels=[])

# next two lines needed to reverse x axis:
ax1.set_xlim(ax1.get_xlim()[::-1]) 


# ANIONS
subplot(1,3,3)
fill([100,100,0,100],[0,100,100,0],color = (0.8,0.8,0.8))
plot([0, 100],[100, 0],'k')
plot([50, 50, 0, 50],[0, 50, 50, 0],'k--')
text(55,15, 'Cl type')
text(5,15, 'HCO3 type')
text(5,65, 'SO4 type')

# loop to use different symbol marker for each water type
for i in range(0, nosamples):
    if obs[i, 0] > 0:
        h1=plot(100*obs[i,Cl]/(obs[i,EC]/100), 100*obs[i,SO4]/(obs[i,EC]/100), 'ro', ms = markersize)
#    if obs[i, 0] == 2:
#        h2=plot(100*obs[i,Cl]/(obs[i,EC]/100), 100*obs[i,SO4]/(obs[i,EC]/100), 'b>', ms = markersize)
#    if obs[i, 0] == 3:
#        h3=plot(100*obs[i,Cl]/(obs[i,EC]/100), 100*obs[i,SO4]/(obs[i,EC]/100), 'c<', ms = markersize)
#    if obs[i, 0] == 4:
#        h4=plot(100*obs[i,Cl]/(obs[i,EC]/100), 100*obs[i,SO4]/(obs[i,EC]/100), 'go', ms = markersize)
#    if obs[i, 0] == 5:
#        h5=plot(100*obs[i,Cl]/(obs[i,EC]/100), 100*obs[i,SO4]/(obs[i,EC]/100), 'm^', ms = markersize)
xlim(0,100)
ylim(0,100)
xlabel('Cl (% meq) =>')
ylabel('SO4 (% meq) =>')


# CATIONS AND ANIONS COMBINED IN DIAMOND SHAPE PLOT = BOX IN RECTANGULAR COORDINATES
# 2 lines below needed to create 2nd y-axis (ax1b) for first subplot
ax2 = fig.add_subplot(132)
ax2b = ax2.twinx()

ax2.plot([0, 100],[10, 10],'k--')
ax2.plot([0, 100],[50, 50],'k--')
ax2.plot([0, 100],[90, 90],'k--')
ax2.plot([10, 10],[0, 100],'k--')
ax2.plot([50, 50],[0, 100],'k--')
ax2.plot([90, 90],[0, 100],'k--')

# loop to use different symbol marker for each water type
for i in range(0, nosamples):
    if obs[i, 0] > 0:
        h1=ax2.plot(100*obs[i,NaK]/(obs[i,EC]/100), 100*(obs[i,SO4]+obs[i,Cl])/(obs[i,EC]/100), 'ro', ms = markersize)
#    if obs[i, 0] == 2:
#        h2=ax2.plot(100*obs[i,NaK]/(obs[i,EC]/100), 100*(obs[i,SO4]+obs[i,Cl])/(obs[i,EC]/100), 'b>', ms = markersize)
#    if obs[i, 0] == 3:
#        h3=ax2.plot(100*obs[i,NaK]/(obs[i,EC]/100), 100*(obs[i,SO4]+obs[i,Cl])/(obs[i,EC]/100), 'c<', ms = markersize)
#    if obs[i, 0] == 4:
#        h4=ax2.plot(100*obs[i,NaK]/(obs[i,EC]/100), 100*(obs[i,SO4]+obs[i,Cl])/(obs[i,EC]/100), 'go', ms = markersize)
#    if obs[i, 0] == 5:
#        h5=ax2.plot(100*obs[i,NaK]/(obs[i,EC]/100), 100*(obs[i,SO4]+obs[i,Cl])/(obs[i,EC]/100), 'm^', ms = markersize)

ax2.set_xlim(0,100)
ax2.set_ylim(0,100)
ax2.set_xlabel('Na+K (% meq) =>')
ax2.set_ylabel('SO4+Cl (% meq) =>')
ax2.set_title('<= Ca+Mg (% meq)', fontsize = 12)
ax2b.set_ylabel('<= CO3+HCO3 (% meq)')
ax2b.set_ylim(0,100)
# next two lines needed to reverse 2nd y axis:
ax2b.set_ylim(ax2b.get_ylim()[::-1])

# Legend for Figure
#figlegend((h1,h2,h3,h4,h5),('Dinkel','Tributaries NL','Tributaries G','Lakes','Groundwater'), ncol=5, shadow=False, fancybox=True, loc='lower center', handlelength = 3)

# adjust position subplots
subplots_adjust(left=0.05, bottom=0.2, right=0.95, top=0.90, wspace=0.4, hspace=0.0)
show()