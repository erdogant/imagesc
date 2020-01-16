# imagesc

[![Python](https://img.shields.io/pypi/pyversions/imagesc)](https://img.shields.io/pypi/pyversions/imagesc)
[![PyPI Version](https://img.shields.io/pypi/v/imagesc)](https://pypi.org/project/imagesc/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/imagesc/blob/master/LICENSE)
[![Downloads](https://pepy.tech/badge/imagesc/week)](https://pepy.tech/project/imagesc/week)

* imagesc is an Python package to create heatmaps. Various methods to create a heatmap are implemented, each with specific properties that can help to easily create your heatmap. The **fast** and **fastclean** method is optimized for speed, the **cluster** method provides clustering, the **seaborn** method contains many configuration settings, and finally, the **plot** as good as possible the imagesc from matlab.

### Functions in imagesc
```python
# data is your numpy array
fig = imagesc.seaborn(data)
fig = imagesc.cluster(data)
fig = imagesc.fast(data)
fig = imagesc.clean(data)
fig = imagesc.plot(data)
status = imagesc.savefig(fig)
```

## Contents
- [Installation](#-installation)
- [Requirements](#-Requirements)
- [Quick Start](#-quick-start)
- [Contribute](#-contribute)
- [Citation](#-citation)
- [Maintainers](#-maintainers)
- [License](#-copyright)

## Installation
* Install imagesc from PyPI (recommended). imagesc is compatible with Python 3.6+ and runs on Linux, MacOS X and Windows. 
* It is distributed under the MIT license.

## Requirements
```python
pip install numpy pandas matplotlib seaborn
Note that: seaborn is only required when using **seaborn** or **cluster** functions.
or
pip install -r requirements.txt
```

## Quick Start
```
pip install imagesc
```

* Alternatively, install imagesc from the GitHub source:
```bash
git clone https://github.com/erdogant/imagesc.git
cd imagesc
python setup.py install
```  

### Import imagesc package
```python
import imagesc as imagesc
```

#### seaborn - The heatmap implemented using **seaborn** contains a large number of configurations possibilities. 
* Slow when using large datasets.
* Grid is aligned to the cells
* See here for all parameters: https://seaborn.pydata.org/generated/seaborn.heatmap.html

```python
df = pd.DataFrame(np.random.randint(0,100,size=(10,20)))
A = imagesc.seaborn(df.values, df.index.values, df.columns.values)
B = imagesc.seaborn(df.values, df.index.values, df.columns.values, annot=True, annot_kws={"size": 12})
C = imagesc.seaborn(df.values, df.index.values, df.columns.values, annot=True, annot_kws={"size": 12}, cmap='rainbow')
D = imagesc.seaborn(df.values, df.index.values, df.columns.values, annot=True, annot_kws={"size": 12}, cmap='rainbow', linecolor='#ffffff')
```
<p align="center">
  A<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/seaborn1.png" width="250" />
  B<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/seaborn2.png" width="250" />
  C<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/seaborn3.png" width="250" />
  D<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/seaborn4.png" width="250" />
</p>


#### cluster - The heatmap created using the **cluster** implementation is usefull when you desire to cluster your data. 
* Default distance setting: metric="euclidean", linkage="ward"
* Slow for large data sets
* Grid is aligned to the cells
* Possibilities to tweak
* Possible arguments: https://seaborn.pydata.org/generated/seaborn.clustermap.html

```python
df = pd.DataFrame(np.random.randint(0,100,size=(10,20)))
fig_C1 = imagesc.cluster(df.values, df.index.values, df.columns.values)
fig_C2 = imagesc.cluster(df.values, df.index.values, df.columns.values, cmap='rainbow')
fig_C3 = imagesc.cluster(df.values, df.index.values, df.columns.values, cmap='rainbow', linecolor='#ffffff')
fig_C4 = imagesc.cluster(df.values, df.index.values, df.columns.values, cmap='rainbow', linecolor='#ffffff', linewidth=0)
imagesc.savefig(fig_C1, './docs/figs/cluster4.png')
```
<p align="center">
  C1<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/cluster1.png" width="250" />
  C2<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/cluster2.png" width="250" />
  C3<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/cluster3.png" width="250" />
  C4<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/cluster4.png" width="250" />
</p>


#### fast - The heatmap created using the **fast** implementation
* Fast
* Not so much tweakable
* Grid is **not** aligned to the cells
* Possible arguments: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.pcolorfast.html

```python
df = pd.DataFrame(np.random.randint(0,100,size=(10,20)))
fig_F1 = imagesc.fast(df.values, df.index.values, df.columns.values)
fig_F2 = imagesc.fast(df.values, df.index.values, df.columns.values, grid=False)
fig_F3 = imagesc.fast(df.values, df.index.values, df.columns.values, grid=False, cbar=False)
fig_F4 = imagesc.fast(df.values, df.index.values, df.columns.values, grid=True, cbar=False)
fig_F5 = imagesc.fast(df.values, df.index.values, df.columns.values, cmap='rainbow')
fig_F6 = imagesc.fast(df.values, df.index.values, df.columns.values, cmap='rainbow', linewidth=0.5, grid=True)
imagesc.savefig(fig_C1, './docs/figs/fast1.png')
```
<p align="center">
  F1<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/fast1.png" width="250" />
  F2<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/fast2.png" width="250" />
  F3<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/fast3.png" width="250" />
  F4<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/fast4.png" width="250" />
  F5<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/fast5.png" width="250" />
  F6<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/fast6.png" width="250" />
</p>

#### fastclean - The heatmap created using the **fastclean** implementation is fast and clean with almonst no configurations settings.
* Fast
* Tweakable not so much
* No Grid
* Possible arguments: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.pcolorfast.html

```python
df = pd.DataFrame(np.random.randint(0,100,size=(10,20)))
fig_FC1 = imagesc.fastclean(df.values)
fig_FC2 = imagesc.fastclean(df.values, cmap='rainbow')
imagesc.savefig(fig_C1, './docs/figs/fastclean1.png')
```
<p align="center">
  F1<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/fastclean1.png" width="250" />
  F2<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/fastclean2.png" width="250" />
</p>

#### plot - The heatmap created using the **plot** implementation will behave more-or-less as the one of matlab.
* Medium speed
* Tweakable but less then **seaborn**
* Grid is aligned to the cells
* Possible arguments: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.imshow.html

```python
df = pd.DataFrame(np.random.randint(0,100,size=(10,20)))
fig_M1 = imagesc.plot(df.values)
fig_M2 = imagesc.plot(df.values, cbar=False)
fig_M3 = imagesc.plot(df.values, cbar=False, axis=False)
fig_M4 = imagesc.plot(df.values, cbar=False, axis=True, linewidth=0.2)
fig_M5 = imagesc.plot(df.values, df.index.values, df.columns.values)
fig_M6 = imagesc.plot(df.values, df.index.values, df.columns.values, cbar=False, linewidth=0.2)
fig_M7 = imagesc.plot(df.values, df.index.values, df.columns.values, grid=True, cbar=False, linewidth=0.2)
fig_M8 = imagesc.plot(df.values, df.index.values, df.columns.values, grid=False, cbar=False, linewidth=0.2)
fig_M9 = imagesc.plot(df.values, df.index.values, df.columns.values, grid=True, cbar=False, linewidth=0.8, linecolor='#ffffff')
fig_M10 = imagesc.plot(df.values, df.index.values, df.columns.values, grid=True, cbar=False, linewidth=0.8, linecolor='#ffffff', cmap='rainbow')
imagesc.savefig(fig, './docs/figs/plot10.png')imagesc.savefig(fig_C1, './docs/figs/fast1.png')
```
<p align="center">
  M1<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/plot1.png" width="250" />
  M2<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/plot2.png" width="250" />
  M3<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/plot3.png" width="250" />
  M4<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/plot4.png" width="250" />
  M5<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/plot5.png" width="250" />
  M6<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/plot6.png" width="250" />
  M7<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/plot7.png" width="250" />
  M8<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/plot8.png" width="250" />
  M9<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/plot9.png" width="250" />
  M10<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/plot10.png" width="250" />
</p>


#### Speed:
The heatmap based on plot will behave more-or-less as the one of matlab.
```python
import matplotlib.image as mpimg
img=mpimg.imread('./docs/figs/lenna.png')

fig = imagesc.fastclean(img)
# runtime 1.49

fig = imagesc.fast(img, cbar=False, axis=False)
# runtime: 2.931 seconds

fig = imagesc.plot(img, linewidth=0, cbar=False)
# runtime: 11.042
```

<p align="center">
  **fast**<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/fast_lenna.png" width="250" />
  **fastclean**<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/fastclean_lenna.png" width="250" />
  **plot**<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/plot_lenna1.png" width="250" />
</p>



## Citation
Please cite imagesc in your publications if this is useful for your research. Here is an example BibTeX entry:
```BibTeX
@misc{erdogant2019imagesc,
  title={imagesc},
  author={Erdogan Taskesen},
  year={2019},
  howpublished={\url{https://github.com/erdogant/imagesc}},
}
```

## References
* seaborn
https://seaborn.pydata.org/generated/seaborn.heatmap.html
* clustermap
https://seaborn.pydata.org/generated/seaborn.clustermap.html
* fast and fastclean
https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.pcolor.html
* plot
 https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.imshow.html
* Other
https://matplotlib.org/3.1.1/gallery/images_contours_and_fields/image_annotated_heatmap.html
* Colormap
https://matplotlib.org/examples/color/colormaps_reference.html


## Maintainers
* Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)

## Contribute
* Contributions are welcome.

## © Copyright
See [LICENSE](LICENSE) for details.
