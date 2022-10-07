from imagesc.imagesc import (
    d3,
    seaborn,
    cluster,
    fast,
    clean,
    plot)

from imagesc.utils.savefig import savefig

from imagesc.utils.adjmat_vec import (
    vec2adjmat,
    adjmat2vec,
    )

__author__ = 'Erdogan Tasksen'
__email__ = 'erdogant@gmail.com'
__version__ = '0.3.0'

# module level doc-string
__doc__ = """
imagesc - imagesc is an Python package to create heatmaps in a easy way.
=========================================================================

Examples
--------
>>> # Import libraries
>>> import pandas as pd
>>> import imagesc as imagesc
>>> # Create example dataset
>>> df = pd.DataFrame(pd.np.random.rand(3,4), columns=['aap', 'boom', 'mies','banaan'] , index=['aap1', 'boom2', 'mies3'])
>>>
>>> # Example: Seaborn
>>> fig, ax = imagesc.seaborn(df.values, df.index.values, df.columns.values)
>>>
>>> # Example: Clustering
>>> fig = imagesc.cluster(df.values, df.index.values, df.columns.values)
>>>
>>> # Example: When speed matters
>>> fig, ax = imagesc.fast(df.values, df.index.values, df.columns.values)
>>>
>>> # Plot example
>>> fig, ax = imagesc.plot(df.values, df.index.values, df.columns.values)
>>>
>>> # Example: Save figure
>>> status = imagesc.savefig(fig)
>>>
>>> Example: Heatmap in d3js
>>> df = pd.DataFrame(np.random.randint(0, 100, size=(50, 50)))
>>> imagesc.d3(df, vmax=1)
>>>

References
----------
* d3blocks: d3blocks.github.io/d3blocks/
* d3blocks (blog): https://towardsdatascience.com/creating-beautiful-stand-alone-interactive-d3-charts-with-python-804117cb95a7
"""
