# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 08:37:59 2020

@author: Erdogan
"""
# %reset -f
# import etutils as et
import pandas as pd
import numpy as np
import imagesc as imagesc

# %%
df = pd.DataFrame(np.zeros((5, 10)).astype(int))
df.iloc[0,0]=10
df.iloc[1,1]=11
df.iloc[2,2]=22
df.iloc[3,3]=33
df.iloc[4,4]=44
df.iloc[3,4]=34
df.iloc[4,9]=39
df.iloc[0,9]=90
imagesc.d3(df, fontsize=10, title='Hooray!', description='python to d3 conversion!', path='d3heatmap.html', width=600, height=300, cmap='interpolateGreens', vmin=1)

# %%
df = pd.DataFrame(np.random.randint(0, 10, size=(7, 52)))
imagesc.d3(df, fontsize=10, title='Hooray!', description='python to d3 conversion!', path='d3heatmap.html', height=200, width=750, cmap='interpolateGreens')
imagesc.d3(df, fontsize=10, title='Hooray!', description='python to d3 conversion!', path='d3heatmap.html', height=200, width=750, cmap='interpolateGreens', vmin=8, vmax=10)
imagesc.d3(df, fontsize=10, title='Hooray!', description='python to d3 conversion!', path='d3heatmap.html', height=200, width=750, cmap='interpolateGreens', scale=True, vmin=80, vmax=100)

imagesc.d3(df, fontsize=10, title='Hooray!', description='python to d3 conversion!', path='d3heatmap.html', height=200, width=750, cmap='interpolateGreens', scale=True)

imagesc.d3(df, fontsize=10, title='Hooray!', description='python to d3 conversion!', path='d3heatmap.html', height=200, width=750, cmap='interpolateGreens', scale=False, vmin=None, vmax=None)
imagesc.d3(df, fontsize=10, title='Hooray!', description='python to d3 conversion!', path='d3heatmap.html', height=200, width=750, cmap='interpolateGreens', scale=False, stroke='black')
imagesc.d3(df, fontsize=10, title='Hooray!', description='python to d3 conversion!', path='d3heatmap.html', height=200, width=750, cmap='interpolateGreens', scale=False, stroke='red', vmin=None, vmax=None)

# %%
# df = pd.DataFrame(np.random.rand(10,15))
df = pd.DataFrame(np.random.randint(0,100,size=(6,20)))
# df = pd.DataFrame(np.random.randint(0,100,size=(5,25)))
# df = pd.DataFrame(np.random.randint(0,100,size=(10,100)))

fig = imagesc.seaborn(df.values, df.index.values, df.columns.values, annot=True, annot_kws={"size": 12})

# %% Seaborn

import imagesc as imagesc
fig = imagesc.seaborn(df.values, df.index.values, df.columns.values, title='test', xlabel='xlabel', ylabel='ylabel')
# imagesc.savefig(fig, './docs/figs/seaborn1.png')
fig = imagesc.seaborn(df.values, df.index.values, df.columns.values, annot=True, annot_kws={"size": 12})
# imagesc.savefig(fig, './docs/figs/seaborn2.png')
fig = imagesc.seaborn(df.values, df.index.values, df.columns.values, annot=True, annot_kws={"size": 12}, cmap='rainbow')
# imagesc.savefig(fig, './docs/figs/seaborn3.png')
fig = imagesc.seaborn(df.values, df.index.values, df.columns.values, annot=True, annot_kws={"size": 12}, cmap='rainbow', linecolor='#ffffff')
# imagesc.savefig(fig, './docs/figs/seaborn4.png')
fig = imagesc.seaborn(df.values, df.index.values, df.columns.values, annot=True, annot_kws={"size": 12}, cmap='rainbow', linecolor='#ffffff', linewidth=0)
# imagesc.savefig(fig, './docs/figs/seaborn5.png')
# print('[%.3f] Seaborn' %(et.toc()))

# fig = imagesc.seaborn(df.values, df.index.values, df.columns.values, annot=True, annot_kws={"size": 12}, cmap='rainbow', linecolor='#ffffff', linewidth=0, ytickRot=45, xtickRot=45)

# %% Cluster
import imagesc as imagesc
fig = imagesc.cluster(df.values, df.index.values, df.columns.values, title='test', xlabel='xlabel', ylabel='ylabel')
# imagesc.savefig(fig, './docs/figs/cluster1.png')
fig = imagesc.cluster(df.values, df.index.values, df.columns.values, cmap='rainbow')
# imagesc.savefig(fig, './docs/figs/cluster2.png')
fig = imagesc.cluster(df.values, df.index.values, df.columns.values, cmap='rainbow', linecolor='#ffffff')
# imagesc.savefig(fig, './docs/figs/cluster3.png')
fig = imagesc.cluster(df.values, df.index.values, df.columns.values, cmap='rainbow', linecolor='#ffffff', linewidth=0)
# imagesc.savefig(fig, './docs/figs/cluster4.png')
# print('[%.3f] Cluster' %(et.toc()))

# fig = imagesc.cluster(df.values, df.index.values, df.columns.values, cmap='rainbow', linecolor='#ffffff', linewidth=0, ytickRot=45, xtickRot=45)

# %% Fast
import imagesc as imagesc
fig = imagesc.fast(df.values, df.index.values, df.columns.values, title='test', xlabel='xlabel', ylabel='ylabel')
# imagesc.savefig(fig, './docs/figs/fast1.png')
fig = imagesc.fast(df.values, df.index.values, df.columns.values, grid=False)
# imagesc.savefig(fig, './docs/figs/fast2.png')
fig = imagesc.fast(df.values, df.index.values, df.columns.values, grid=False, cbar=False)
# imagesc.savefig(fig, './docs/figs/fast3.png')
fig = imagesc.fast(df.values, df.index.values, df.columns.values, grid=True, cbar=False)
# imagesc.savefig(fig, './docs/figs/fast4.png')
fig = imagesc.fast(df.values, df.index.values, df.columns.values, cmap='rainbow')
# imagesc.savefig(fig, './docs/figs/fast5.png')
fig = imagesc.fast(df.values, df.index.values, df.columns.values, cmap='rainbow', linewidth=0.5, grid=True)
# imagesc.savefig(fig, './docs/figs/fast6.png')

# fig = imagesc.fast(df.values, df.index.values, df.columns.values, cmap='rainbow', linewidth=0.5, grid=True, ytickRot=45, xtickRot=45)

# %% Clean: Best for plotting photos
import imagesc as imagesc
fig = imagesc.clean(df.values)
# imagesc.savefig(fig, './docs/figs/clean1.png')
fig = imagesc.clean(df.values, cmap='rainbow')
# imagesc.savefig(fig, './docs/figs/clean2.png')

# %% Matlab-like plots

# df = pd.DataFrame(np.random.randint(0,100,size=(50,50)))
import imagesc as imagesc

fig = imagesc.plot(df.values, title='test', xlabel='xlabel', ylabel='ylabel')
# imagesc.savefig(fig, './docs/figs/plot1.png')
fig = imagesc.plot(df.values, cbar=False)
# imagesc.savefig(fig, './docs/figs/plot2.png')
fig = imagesc.plot(df.values, cbar=False, axis=False)
# imagesc.savefig(fig, './docs/figs/plot3.png')
fig = imagesc.plot(df.values, cbar=False, axis=True, linewidth=0.2)
# imagesc.savefig(fig, './docs/figs/plot4.png')
fig = imagesc.plot(df.values, df.index.values, df.columns.values)
# imagesc.savefig(fig, './docs/figs/plot5.png')
fig = imagesc.plot(df.values, df.index.values, df.columns.values, cbar=False, linewidth=0.2)
# imagesc.savefig(fig, './docs/figs/plot6.png')
fig = imagesc.plot(df.values, df.index.values, df.columns.values, grid=True, cbar=False, linewidth=0.2)
# imagesc.savefig(fig, './docs/figs/plot7.png')
fig = imagesc.plot(df.values, df.index.values, df.columns.values, grid=False, cbar=False, linewidth=0.2)
# imagesc.savefig(fig, './docs/figs/plot8.png')
fig = imagesc.plot(df.values, df.index.values, df.columns.values, grid=True, cbar=False, linewidth=0.8, linecolor='#ffffff')
# imagesc.savefig(fig, './docs/figs/plot9.png')
fig = imagesc.plot(df.values, df.index.values, df.columns.values, grid=True, cbar=False, linewidth=0.8, linecolor='#ffffff', cmap='rainbow')
# imagesc.savefig(fig, './docs/figs/plot10.png')


# %% Photo image
import matplotlib.image as mpimg
img=mpimg.imread('./docs/figs/lenna.png')

# et.tic()
fig = imagesc.fast(img, cbar=False, axis=False)
imagesc.savefig(fig, './docs/figs/fast_lenna.png')
# print('[%.3f] fast' %(et.toc()))

# et.tic()
fig = imagesc.clean(img)
# print('[%.3f] clean' %(et.toc()))

# et.tic()
fig = imagesc.plot(img, linewidth=0, cbar=False, axis=False)
imagesc.savefig(fig, './docs/figs/plot_lenna1.png')
# print('[%.3f] plot' %(et.toc()))

#%% Timings with arrays
from tqdm import tqdm
t_seaborn=[]
t_cluster=[]
t_fast=[]
t_clean=[]
t_plot=[]
arraysizes=np.arange(50,1250,250)

for i in tqdm(arraysizes):
    arrsize=(i,i)
    df = pd.DataFrame(np.random.randint(0,100,size=arrsize))

    et.tic()
    fig = imagesc.seaborn(df.values, verbose=0)
    t_seaborn.append(et.toc())
    
    et.tic()
    fig = imagesc.cluster(df.values, verbose=0)
    t_cluster.append(et.toc())
    
    et.tic()
    fig = imagesc.fast(df.values, verbose=0)
    t_fast.append(et.toc())
    
    et.tic()
    fig = imagesc.clean(df.values, verbose=0)
    t_clean.append(et.toc())
    
    et.tic()
    fig = imagesc.plot(df.values, verbose=0)
    t_plot.append(et.toc())

plt.figure(figsize=(20,8))
plt.plot(t_seaborn, label='seaborn')
plt.plot(t_cluster, label='cluster (clustermap)')
plt.plot(t_fast, label='fast (pcolorfast)')
plt.plot(t_fastclean, label='clean (pcolorfast)')
plt.plot(t_plot, label='plot (imshow)')
plt.legend()
plt.xlabel('array size')
plt.ylabel('time in seconds')
plt.xticks(ticks=np.arange(0,len(arraysizes)), labels=arraysizes)
imagesc.savefig(fig, './docs/figs/time_in_secs.png')

