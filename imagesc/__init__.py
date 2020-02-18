from imagesc.imagesc import (
    seaborn,
    cluster,
    fast,
    clean,
    plot)

from imagesc.savefig import savefig

__author__ = 'Erdogan Tasksen'
__email__ = 'erdogant@gmail.com'
__version__ = '0.1.7'

# module level doc-string
__doc__ = """
imagesc - imagesc is an Python package to create heatmaps in a easy way.
=========================================================================

Examples
--------
>>>
>>> import pandas as pd
>>> df = pd.DataFrame(pd.np.random.rand(3,4), columns=['aap', 'boom', 'mies','banaan'] , index=['aap1', 'boom2', 'mies3'])
>>>
>>> import imagesc as imagesc
>>>
>>>
>>> # Seaborn example
>>> fig = imagesc.seaborn(df.values, df.index.values, df.columns.values)
>>>
>>> # Cluster example
>>> fig = imagesc.cluster(df.values, df.index.values, df.columns.values)
>>>
>>> # Fast example
>>> fig = imagesc.fast(df.values, df.index.values, df.columns.values)
>>>
>>> # Plot example
>>> fig = imagesc.plot(df.values, df.index.values, df.columns.values)
>>>
>>> status = imagesc.savefig(fig)
>>>


References
----------
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


"""
