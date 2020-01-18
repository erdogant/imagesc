# imagesc

[![Python](https://img.shields.io/pypi/pyversions/imagesc)](https://img.shields.io/pypi/pyversions/imagesc)
[![PyPI Version](https://img.shields.io/pypi/v/imagesc)](https://pypi.org/project/imagesc/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/imagesc/blob/master/LICENSE)
[![Downloads](https://pepy.tech/badge/imagesc/week)](https://pepy.tech/project/imagesc/week)

* imagesc is an Python package to create heatmaps. Various methods to create a heatmap are implemented, each with specific properties that can help to easily create your heatmap. The **fast** and **clean** method is optimized for speed, the **cluster** method provides clustering, the **seaborn** method contains many configuration settings, and finally, the **plot** as good as possible the imagesc from matlab.

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
# Note that: seaborn is only required when using **seaborn** or **cluster** functions.
pip install numpy pandas matplotlib seaborn
# or
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

## Import imagesc package
```python
import imagesc as imagesc
```

## seaborn
* Underlying implemented is based on **seaborn**
* Large number of configurations
* Slow when using large datasets
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
  A<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/seaborn1.png" width="300" />
  B<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/seaborn2.png" width="300" />
  C<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/seaborn3.png" width="300" />
  D<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/seaborn4.png" width="300" />
</p>


## cluster
* Underlying implemented is based on **clustermap** 
* When you desire to cluster your heatmap
* Default distance setting: metric="euclidean", linkage="ward" (can be changed)
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
  C1<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/cluster1.png" width="300" />
  C2<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/cluster2.png" width="300" />
  C3<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/cluster3.png" width="300" />
  C4<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/cluster4.png" width="300" />
</p>


## fast
* Underlying implemented is based on **pcolorfast** 
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
  F1<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/fast1.png" width="300" />
  F2<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/fast2.png" width="300" />
  F3<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/fast3.png" width="300" />
  F4<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/fast4.png" width="300" />
  F5<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/fast5.png" width="300" />
  F6<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/fast6.png" width="300" />
</p>

## clean
* Underlying implemented is based on **pcolorfast** 
* Fast
* No Grid
* Limited configurations
* Ideal for photos
* Possible arguments: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.pcolorfast.html

```python
df = pd.DataFrame(np.random.randint(0,100,size=(10,20)))
fig_FC1 = imagesc.clean(df.values)
fig_FC2 = imagesc.clean(df.values, cmap='rainbow')
imagesc.savefig(fig_C1, './docs/figs/clean1.png')
```
<p align="center">
  F1<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/clean1.png" width="300" />
  F2<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/clean2.png" width="300" />
</p>

## plot
* Underlying implemented is based on **imshow** 
* implementation will behave more-or-less as the one of matlab
* Medium speed
* Various configurations are possible but less then **seaborn**
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
  M1<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/plot1.png" width="300" />
  M2<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/plot2.png" width="300" />
  M3<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/plot3.png" width="300" />
  M4<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/plot4.png" width="300" />
  M5<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/plot5.png" width="300" />
  M6<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/plot6.png" width="300" />
  M7<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/plot7.png" width="300" />
  M8<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/plot8.png" width="300" />
  M9<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/plot9.png" width="300" />
  M10<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/plot10.png" width="300" />
</p>


## Speed:
```python
import matplotlib.image as mpimg
img=mpimg.imread('./docs/figs/lenna.png')

fig = imagesc.clean(img)
# runtime 1.49

fig = imagesc.fast(img, cbar=False, axis=False)
# runtime: 2.931 seconds

fig = imagesc.plot(img, linewidth=0, cbar=False)
# runtime: 11.042
```
<p align="center">
  **fast**<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/fast_lenna.png" width="300" />
  **clean**<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/clean_lenna.png" width="300" />
  **plot**<img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/plot_lenna1.png" width="300" />
</p>
<p align="center">
  <img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/time_in_secs.png" width="1000" />
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
* fast and clean
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

## Licence
See [LICENSE](LICENSE) for details.
