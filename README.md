# imagesc

[![Python](https://img.shields.io/pypi/pyversions/imagesc)](https://img.shields.io/pypi/pyversions/imagesc)
[![PyPI Version](https://img.shields.io/pypi/v/imagesc)](https://pypi.org/project/imagesc/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/imagesc/blob/master/LICENSE)

* imagesc is an Python package to create heatmaps.

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
* It is advisable to create a new environment. 
```python
conda create -n env_imagesc python=3.6
conda activate env_imagesc
pip install numpy pandas tqdm matplotlib
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
df = pd.read_csv('https://github.com/erdogant/hnet/blob/master/imagesc/data/example_data.csv')
model = imagesc.fit(df)
G = imagesc.plot(model)
```
<p align="center">
  <img src="https://github.com/erdogant/imagesc/blob/master/docs/figs/fig1.png" width="600" />
  
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
* 
   
## Maintainers
* Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)

## Contribute
* Contributions are welcome.

## © Copyright
See [LICENSE](LICENSE) for details.
