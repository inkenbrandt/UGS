# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 13:39:32 2014

@author: paulinkenbrandt
"""

import pandas as pd
from pylab import *
import matplotlib.pyplot as plt



df = pd.io.excel.read_excel("C:\\PROJECTS\\PAROWAN\\USGS.xlsx","Results",index=1)

grouped = df.groupby('site_no').filter(lambda x: len(x) > 1)



for i, group in df.groupby('site_no'):
    plt.figure()
    group.plot(x='lev_dt',y='lev_va',title=str(i))
    ax = plt.gca()
    ax.set_ylim(ax.get_ylim()[::-1])        
    plt.ylabel("Depth to Water (ft)")
    plt.savefig("C:\\PROJECTS\\PAROWAN\\Graphs\\"+str(i)+".pdf",format="pdf")

