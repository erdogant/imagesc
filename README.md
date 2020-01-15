# imagesc

[![Python](https://img.shields.io/pypi/pyversions/imagesc)](https://img.shields.io/pypi/pyversions/imagesc)
[![PyPI Version](https://img.shields.io/pypi/v/imagesc)](https://pypi.org/project/imagesc/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/imagesc/blob/master/LICENSE)
[![Downloads](https://pepy.tech/badge/imagesc/week)](https://pepy.tech/project/imagesc/week)

* imagesc is an Python package to create heatmaps. Multiple different manners are implemented, each with specific properties that can help to easily create your heatmap. the **fast** and **fastclean** method is optimized for speed, the **cluster** method allows direct clustering, the **seaborn** method contains many configuration settings, and finally, the **plot** resamples the imagesc from matlab.

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
pip install seaborn numpy pandas matplotlib
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

### Example:
```python
df = pd.DataFrame(np.random.randint(0,100,size=(10,20)))
fig = imagesc.seaborn(df.values, df.index.values, df.columns.values)
```
<p align="center">
  <img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/seaborn1.png" width="300" />
  <img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/seaborn2.png" width="300" />
  <img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/seaborn3.png" width="300" />
  <img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/seaborn4.png" width="300" />
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
