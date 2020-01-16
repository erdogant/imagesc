# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 08:37:59 2020

@author: Erdogan
"""
# %reset -f
import etutils as et
import pandas as pd
import numpy as np
import imagesc as imagesc

# %%
# df = pd.DataFrame(np.random.rand(10,15))
df = pd.DataFrame(np.random.randint(0,100,size=(6,20)))
# df = pd.DataFrame(np.random.randint(0,100,size=(5,25)))
# df = pd.DataFrame(np.random.randint(0,100,size=(10,100)))

# %% Seaborn

et.tic()
import imagesc as imagesc
fig = imagesc.seaborn(df.values, df.index.values, df.columns.values)
imagesc.savefig(fig, './docs/figs/seaborn1.png')
fig = imagesc.seaborn(df.values, df.index.values, df.columns.values, annot=True, annot_kws={"size": 12})
imagesc.savefig(fig, './docs/figs/seaborn2.png')
fig = imagesc.seaborn(df.values, df.index.values, df.columns.values, annot=True, annot_kws={"size": 12}, cmap='rainbow')
imagesc.savefig(fig, './docs/figs/seaborn3.png')
fig = imagesc.seaborn(df.values, df.index.values, df.columns.values, annot=True, annot_kws={"size": 12}, cmap='rainbow', linecolor='#ffffff')
imagesc.savefig(fig, './docs/figs/seaborn4.png')
fig = imagesc.seaborn(df.values, df.index.values, df.columns.values, annot=True, annot_kws={"size": 12}, cmap='rainbow', linecolor='#ffffff', linewidth=0)
imagesc.savefig(fig, './docs/figs/seaborn5.png')
print('[%.3f] Seaborn' %(et.toc()))

# fig = imagesc.seaborn(df.values, df.index.values, df.columns.values, annot=True, annot_kws={"size": 12}, cmap='rainbow', linecolor='#ffffff', linewidth=0, ytickRot=45, xtickRot=45)

# %% Cluster
et.tic()
import imagesc as imagesc
fig = imagesc.cluster(df.values, df.index.values, df.columns.values)
imagesc.savefig(fig, './docs/figs/cluster1.png')
fig = imagesc.cluster(df.values, df.index.values, df.columns.values, cmap='rainbow')
imagesc.savefig(fig, './docs/figs/cluster2.png')
fig = imagesc.cluster(df.values, df.index.values, df.columns.values, cmap='rainbow', linecolor='#ffffff')
imagesc.savefig(fig, './docs/figs/cluster3.png')
fig = imagesc.cluster(df.values, df.index.values, df.columns.values, cmap='rainbow', linecolor='#ffffff', linewidth=0)
imagesc.savefig(fig, './docs/figs/cluster4.png')
print('[%.3f] Cluster' %(et.toc()))

# fig = imagesc.cluster(df.values, df.index.values, df.columns.values, cmap='rainbow', linecolor='#ffffff', linewidth=0, ytickRot=45, xtickRot=45)

# %% Fast
et.tic()
import imagesc as imagesc
fig = imagesc.fast(df.values, df.index.values, df.columns.values)
imagesc.savefig(fig, './docs/figs/fast1.png')
fig = imagesc.fast(df.values, df.index.values, df.columns.values, grid=False)
imagesc.savefig(fig, './docs/figs/fast2.png')
fig = imagesc.fast(df.values, df.index.values, df.columns.values, grid=False, cbar=False)
imagesc.savefig(fig, './docs/figs/fast3.png')
fig = imagesc.fast(df.values, df.index.values, df.columns.values, grid=True, cbar=False)
imagesc.savefig(fig, './docs/figs/fast4.png')
fig = imagesc.fast(df.values, df.index.values, df.columns.values, cmap='rainbow')
imagesc.savefig(fig, './docs/figs/fast5.png')
fig = imagesc.fast(df.values, df.index.values, df.columns.values, cmap='rainbow', linewidth=0.5, grid=True)
imagesc.savefig(fig, './docs/figs/fast6.png')
print('[%.3f] Fast' %(et.toc()))

# fig = imagesc.fast(df.values, df.index.values, df.columns.values, cmap='rainbow', linewidth=0.5, grid=True, ytickRot=45, xtickRot=45)

# %% Clean: Best for plotting photos
et.tic()
import imagesc as imagesc
fig = imagesc.fastclean(df.values)
imagesc.savefig(fig, './docs/figs/fastclean1.png')
fig = imagesc.fastclean(df.values, cmap='rainbow')
imagesc.savefig(fig, './docs/figs/fastclean2.png')
print('[%.3f] Clean and fast' %(et.toc()))

# %% Matlab-like plots
et.tic()

# df = pd.DataFrame(np.random.randint(0,100,size=(50,50)))
import imagesc as imagesc

fig = imagesc.plot(df.values)
imagesc.savefig(fig, './docs/figs/plot1.png')
fig = imagesc.plot(df.values, cbar=False)
imagesc.savefig(fig, './docs/figs/plot2.png')
fig = imagesc.plot(df.values, cbar=False, axis=False)
imagesc.savefig(fig, './docs/figs/plot3.png')
fig = imagesc.plot(df.values, cbar=False, axis=True, linewidth=0.2)
imagesc.savefig(fig, './docs/figs/plot4.png')
fig = imagesc.plot(df.values, df.index.values, df.columns.values)
imagesc.savefig(fig, './docs/figs/plot5.png')
fig = imagesc.plot(df.values, df.index.values, df.columns.values, cbar=False, linewidth=0.2)
imagesc.savefig(fig, './docs/figs/plot6.png')
fig = imagesc.plot(df.values, df.index.values, df.columns.values, grid=True, cbar=False, linewidth=0.2)
imagesc.savefig(fig, './docs/figs/plot7.png')
fig = imagesc.plot(df.values, df.index.values, df.columns.values, grid=False, cbar=False, linewidth=0.2)
imagesc.savefig(fig, './docs/figs/plot8.png')
fig = imagesc.plot(df.values, df.index.values, df.columns.values, grid=True, cbar=False, linewidth=0.8, linecolor='#ffffff')
imagesc.savefig(fig, './docs/figs/plot9.png')
fig = imagesc.plot(df.values, df.index.values, df.columns.values, grid=True, cbar=False, linewidth=0.8, linecolor='#ffffff', cmap='rainbow')
imagesc.savefig(fig, './docs/figs/plot10.png')

print('[%.3f] Default' %(et.toc()))

# %% Photo image
import matplotlib.image as mpimg
img=mpimg.imread('./docs/figs/lenna.png')

et.tic()
fig = imagesc.fast(img, cbar=False, axis=False)
imagesc.savefig(fig, './docs/figs/fast_lenna.png')
print('[%.3f] fast' %(et.toc()))

et.tic()
fig = imagesc.fastclean(img)
print('[%.3f] fastclean' %(et.toc()))

et.tic()
fig = imagesc.plot(img, linewidth=0, cbar=False, axis=False)
imagesc.savefig(fig, './docs/figs/plot_lenna1.png')
print('[%.3f] plot' %(et.toc()))

# et.tic()
# fig = imagesc.plot(img, linewidth=0, cbar=False, axis=False)
# # imagesc.savefig(fig, './docs/figs/plot_lenna2.png')
# print('[%.3f] Default' %(et.toc()))
