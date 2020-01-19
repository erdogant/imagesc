""" imagesc is an Python package to create heatmaps in a easy way. Various different manners are implemented to create heatmaps.

   import imagesc as imagesc

   fig = imagesc.seaborn(data, <optional>)
   fig = imagesc.cluster(data, <optional>)
   fig = imagesc.fast(data, <optional>)
   fig = imagesc.clean(data, <optional>)
   fig = imagesc.plot(data, <optional>)
   status = imagesc.savefig(fig)


 INPUT:
 ------

   data:           Numpy array with rows and columns

   row_labels:     A list or array of length N with the labels for the rows.

   col_labels:     A list or array of length M with the labels for the columns.



 OPTIONAL
 --------

   normalize:      Boolean [False,True]: Normalize data per row. x-x_mean  / max()-min()
                   True: Yes
                   False: No (default)

   label_orientation: String: Plot labels above or below plot
                   'above'
                   'below' (default)

   xtickRot:       Integer [0-360]:  Orientation of the labels
                   90: (default)

   ytickRot:       Integer [0-360]:  Orientation of the labels
                   0: (default)

   dpi:            Integer: Resolution of the figure
                   100 (default)

   xlabel:         String: The x-label
                   None: (default)

   ylabel:         String: The y-label
                   None: (default)

   title:          String: The title
                   None: (default)

   figsize:        tuple: (width, height)
                   (10,10): (default)


 SPECIFIC ARGUMENTS
 ------------------

   standard_scale: Boolean [False,True]
                   True: Yes
                   False: No (default)

   annot:          Boolean [True,False]: Show per cell the value (does not work with clustering)
                   True:
                   False: (default)

   grid:           Boolean [True,False]: Show grid
                   True (Default)
                   False

   axis:           Boolean [True,False]: Show all axis in the plot
                   True (Default)
                   False

   cbar:           Boolean [True,False]: Show the bar
                   True (Default)
                   False

   linewidth:      Float:  Width of the line
                   0.1: (default)
                   0:   if no lines are desired such as in photos

   linecolor:      String:  linecolor of the line in hex
                   '#000000': (default)
                   '#ffffff': (white)

   vmin:           Float: [0-1] range of colors with minimum value
                   None: (Do not use)

   vmax:           Float: [0-1] range of colors with maximum value
                   None: (Do not use)

   distance:       String: Distance measure for cluster
                   'euclidean' (default)

   linkage:        String: Linkage type for cluster
                   'ward' (default)

   cmap:           String: Colormap
                   'coolwarm'
                   'bwr'        Blue-white-red (default)
                   'RdBu'       Red-white-Blue
                   'binary' or 'binary_r'
                   'seismic'    Blue-white-red
                   'rainbow'
                   'Blues'      white-to-blue
                   'Reds'
                   'Pastel1'    Discrete colors
                   'Paired'     Discrete colors
                   'Set1'       Discrete colors

 OUTPUT
 ------
	dictionary


 DESCRIPTION
 -----------
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


 EXAMPLE
 -------

   import pandas as pd
   import numpy as np
   import imagesc as imagesc

   df = pd.DataFrame(np.random.rand(3,4), columns=['aap', 'boom', 'mies','banaan'] , index=['aap1', 'boom2', 'mies3'])
   fig = imagesc.plot(df.values)

"""
# --------------------------------------------------------------------------
# Name        : imagesc.py
# Author      : E.Taskesen
# Mail        : erdogant@gmail.com
# Date        : Jan. 2020
# Licence     : MIT
# --------------------------------------------------------------------------

# %% Libraries
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# %% Adjust figure size based on input
def _set_figsize(data_shape, figsize):
    data_ratio = np.minimum(5/(data_shape[0]/data_shape[1]), 50)
    out = tuple(np.ceil(np.interp(data_shape-np.min(data_shape), [np.min(figsize), data_ratio], [np.max(figsize), data_ratio])))
    return(out[0], out[1])

def plot(data, row_labels=None, col_labels=None, **args):
    """Heatmap plot.

    Parameters
    ----------
    data : numpy array
        data array.
    row_labels
        A list or array of length N with the labels for the rows.
    col_labels
        A list or array of length M with the labels for the columns.
    **args : TYPE
        Various functionalities that can are directly used as input for seaborn.

    Returns
    -------
    fig.


    """
    assert not isinstance(data, pd.DataFrame), print('[IMAGESC] data input must be numpy array')
    # Set defaults
    args, args_im = _defaults(args)
    # Set figsize based on data shape
    args_im['figsize'] = _set_figsize(data.shape, args_im['figsize'])
    # Linewidth if required
    args['linewidth'] = _check_input(data, args['linewidth'], args_im)
    # Normalize
    data = _normalize(data, args_im)
    # Make plot
    fig, ax = plt.subplots(figsize=args_im['figsize'])
    _ = _heatmap(data, row_labels, col_labels, args_im, **args)
    # Add text into the cells
    # _  = _annotate_heatmap(im, valfmt="{x:.1f} t")
    ax.set_xlabel(args_im['xlabel'])
    ax.set_ylabel(args_im['ylabel'])
    if args_im['title'] is not None:
        ax.set_title(args_im['title'])

    fig.tight_layout()
    plt.show()

    # return
    return(fig)

# %% Seaborn
def seaborn(data, row_labels=None, col_labels=None, **args):
    """Heatmap based on seaborn.

    Parameters
    ----------
    data : numpy array
        data array.
    row_labels
        A list or array of length N with the labels for the rows.
    col_labels
        A list or array of length M with the labels for the columns.
    **args : TYPE
        Various functionalities that can are directly used as input for seaborn.
        https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.pcolor.html


    Returns
    -------
    fig.


    """
    assert not isinstance(data, pd.DataFrame), print('[IMAGESC] data input must be numpy array')
    try:
        import seaborn as sns
    except:
        print('[IMAGESC] Error: seaborn is missing! Try to: pip install seaborn')

    # Set defaults
    args, args_im = _defaults(args)
    # Linewidth if required
    args['linewidth'] = _check_input(data, args['linewidth'], args_im)
    # Normalize
    data = _normalize(data, args_im)

    # Cleaning args
    try:
        args.pop('standard_scale')
        args.pop('distance')
        args.pop('linkage')
    except:
        pass

    # Set row and col labels
    row_labels, col_labels = set_labels(data.shape, row_labels, col_labels)
    # Make dataframe
    df = pd.DataFrame(data=data, index=row_labels, columns=col_labels)
    sns.set(color_codes=True)
    sns.set(font_scale=1.2)
    sns.set_style({"savefig.dpi": args_im['dpi']})
    # Set figsize based on data shape
    # args_im['figsize']=_set_figsize(data.shape, args_im['figsize'])
    [fig, ax] = plt.subplots(figsize=args_im['figsize'])
    # Make heatmap
    ax = sns.heatmap(df, **args)
    # Set labels
    ax.set_xlabel(args_im['xlabel'])
    ax.set_ylabel(args_im['ylabel'])
    if args_im['title'] is not None:
        ax.set_title(args_im['title'])
    # Rotate labels
    # ax.set_xticklabels(col_labels, rotation=args_im['xtickRot'], ha='center', minor=False)
    # ax.set_yticklabels(row_labels, rotation=args_im['ytickRot'], ha='right', minor=False)
    # set the x-axis labels on the top
    if args_im['label_orientation'] == 'above':
        ax.xaxis.tick_top()
    fig = ax.get_figure()
    # Plot
    plt.show()
    # Return
    return(fig)

# %% Cluster
def cluster(data, row_labels=None, col_labels=None, **args):
    """Clustering of the Heatmap based on seaborn.


    Parameters
    ----------
    data : numpy array
        data array.
    row_labels
        A list or array of length N with the labels for the rows.
    col_labels
        A list or array of length M with the labels for the columns.
    **args : TYPE
        Various functionalities that can are directly used as input for seaborn.
        https://seaborn.pydata.org/generated/seaborn.clustermap.html

    Returns
    -------
    fig.


    """
    assert not isinstance(data, pd.DataFrame), print('[IMAGESC] data input must be numpy array')
    try:
        import seaborn as sns
    except:
        print('[IMAGESC] Error: seaborn is missing! Try to: pip install seaborn')

    # Set defaults
    args, args_im = _defaults(args)
    # Linewidth if required
    args['linewidth'] = _check_input(data, args['linewidth'], args_im)
    # Normalize
    data = _normalize(data, args_im)

    # Set row and col labels
    row_labels, col_labels = set_labels(data.shape, row_labels, col_labels)
    # Make dataframe
    df = pd.DataFrame(data=data, index=row_labels, columns=col_labels)
    sns.set(color_codes=True)
    sns.set(font_scale=1.2)
    sns.set_style({"savefig.dpi": args_im['dpi']})
    # Set figsize based on data shape
    # args_im['figsize']=_set_figsize(data.shape, args_im['figsize'])
    # Make heatmap
    g = sns.clustermap(df, method=args['linkage'], metric=args['distance'], col_cluster=True, row_cluster=True, linecolor=args['linecolor'], linewidths=args['linewidth'], cmap=args['cmap'], standard_scale=args['standard_scale'], vmin=args['vmin'], vmax=args['vmax'], figsize=args_im['figsize'])
    # Rotate labels
    plt.setp(g.ax_heatmap.get_xticklabels(), rotation=args_im['xtickRot'], ha='center')
    plt.setp(g.ax_heatmap.get_yticklabels(), rotation=args_im['ytickRot'], ha='center')
    # Set labels
    # ax.set_xlabel(args_im['xlabel'])
    # ax.set_ylabel(args_im['ylabel'])
    # g.set_xticklabels(col_labels, rotation=args_im['xtickRot'], ha='center', minor=False)
    # g.set_yticklabels(row_labels, rotation=args_im['ytickRot'], ha='right', minor=False)
    # plt.rc('xtick', labelsize=14)    # fontsize of the tick labels
    # plt.rc('axes', labelsize=14)    # fontsize of the x and y labels

    # Plot
    plt.show()
    # Return
    return(g.fig)

# %% Clean
def clean(data, row_labels=None, col_labels=None, **args):
    """Clean heatmap figure.


    Parameters
    ----------
    data : numpy array
        data array.
    row_labels
        A list or array of length N with the labels for the rows.
    col_labels
        A list or array of length M with the labels for the columns.
    **args : TYPE
        Various functionalities that can are directly used as input for seaborn.
        cmap, vmin, vmax, normalize

    Returns
    -------
    fig.


    """
    assert not isinstance(data, pd.DataFrame), print('[IMAGESC] data input must be numpy array')
    # Set defaults
    args, args_im = _defaults(args)
    # Linewidth if required
    # args['linewidth']=_check_input(data, args['linewidth'], args_im)
    # Normalize
    data = _normalize(data, args_im)
    # Plot
    # Set figsize based on data shape
    args_im['figsize'] = _set_figsize(data.shape, args_im['figsize'])
    fig, ax = plt.subplots(figsize=args_im['figsize'])
    # Make the plot
    ax.pcolorfast(np.flipud(data), cmap=args['cmap'], vmin=args['vmin'], vmax=args['vmax'], alpha=1)
    # Hide grid lines
    # if args_im['grid']==False:
    ax.grid(False)
    # if args_im['axis']==False:
    plt.axis('off')
    # Hide grid lines
    # plt.axis('off')
    # ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    # Set labels
    ax.set_xlabel(args_im['xlabel'])
    ax.set_ylabel(args_im['ylabel'])

    fig.tight_layout()
    plt.show()
    # Return
    return(fig)

# %% Fast
def fast(data, row_labels=None, col_labels=None, **args):
    """Fast manner to create a Heatmap.

    Parameters
    ----------
    data : numpy array
        data array.
    row_labels
        A list or array of length N with the labels for the rows.
    col_labels
        A list or array of length M with the labels for the columns.
    **args : TYPE
        Various functionalities that can are directly used as input for seaborn.
        cmap, vmin, vmax, normalize


    Returns
    -------
    fig.


    """
    assert not isinstance(data, pd.DataFrame), print('[IMAGESC] data input must be numpy array')
    # Set defaults
    args, args_im = _defaults(args)
    # Linewidth if required
    args['linewidth'] = _check_input(data, args['linewidth'], args_im)
    # Normalize
    data = _normalize(data, args_im)
    # Plot
    # Set figsize based on data shape
    # args_im['figsize']=_set_figsize(data.shape, args_im['figsize'])
    fig, ax = plt.subplots(figsize=args_im['figsize'])

    # print(args_im['figsize'])
    # Make the real plot
    im = ax.pcolorfast(np.flipud(data), cmap=args['cmap'], vmin=args['vmin'], vmax=args['vmax'], alpha=1)

    # Create colorbar
    if args['cbar']:
        ax.figure.colorbar(im, ax=ax)
        # cbar.ax.set_ylabel(cbarlabel='', rotation=-90, va="bottom")
    # Show all ticks and label with the respective list entries.
    if col_labels is not None:
        ax.set_xticks(np.arange(data.shape[1]))
        ax.set_xticklabels(col_labels)
        # Let the horizontal axes labeling appear on top.
        if args_im['label_orientation'] == 'above':
            ax.tick_params(top=True, bottom=True, labeltop=True, labelbottom=False)
        if args_im['label_orientation'] == 'below':
            ax.tick_params(top=True, bottom=True, labeltop=False, labelbottom=True)
        # Rotate the tick labels and set their alignment.
        plt.setp(ax.get_xticklabels(), rotation=args_im['xtickRot'], ha="center", rotation_mode="anchor")

    # Rotate labels
    # ax.set_xticklabels(col_labels, rotation=args_im['xtickRot'], ha='center', minor=False)
    # ax.set_yticklabels(row_labels, rotation=args_im['ytickRot'], ha='right', minor=False)

    if row_labels is not None:
        ax.set_yticks(np.arange(data.shape[0]))
        ax.set_yticklabels(row_labels)
        plt.setp(ax.get_yticklabels(), rotation=args_im['ytickRot'], ha="right", rotation_mode="anchor")

    # Turn spines off and create white grid.
    # for edge, spine in ax.spines.items():
    #     spine.set_visible(False)

    if args_im['grid']:
        ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
        ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    if args['linewidth']>0 and args_im['grid']:
        ax.grid(which="minor", color=args['linecolor'], linestyle='-', linewidth=args['linewidth'])
    if not args_im['axis']:
        plt.axis('off')
    ax.grid(False)

    # Set labels
    ax.set_xlabel(args_im['xlabel'])
    ax.set_ylabel(args_im['ylabel'])
    if args_im['title'] is not None:
        ax.set_title(args_im['title'])

    # Return
    return(fig)

# %%
def _heatmap(data, row_labels, col_labels, args_im, **args):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (N, M).
    row_labels
        A list or array of length N with the labels for the rows.
    col_labels
        A list or array of length M with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **args
        All other arguments are forwarded to `imshow`.
        

    References
    ----------
    https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.pcolor.html
    https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.imshow.html
    
    """
    # Cleaning args
    try:
        args_im['linewidth']=args['linewidth']
        args.pop('linewidth')
        args_im['linecolor']=args['linecolor']
        args.pop('linecolor')
        args_im['cbar']=args['cbar']
        args.pop('cbar')
        args.pop('standard_scale')
        args.pop('distance')
        args.pop('linkage')
        args.pop('annot')
        args.pop('annot_kws')
    except:
        pass

    ax=None
    # cbar_kw={}
    # cbarlabel=""

    if not ax:
        ax = plt.gca()
        
    # Plot the heatmap
    im = ax.imshow(data, **args)

    # Create colorbar
    if args_im['cbar']:
        # cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
        # cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")
        # create an axes on the right side of ax. The width of cax will be 5%
        # of ax and the padding between cax and ax will be fixed at 0.05 inch.
        from mpl_toolkits.axes_grid1 import make_axes_locatable
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        plt.colorbar(im, cax=cax)

    # We want to show all ticks...
    if not col_labels is None:
        ax.set_xticks(np.arange(data.shape[1]))
        ax.set_xticklabels(col_labels)
        # Let the horizontal axes labeling appear on top.
        if args_im['label_orientation']=='above':
            ax.tick_params(top=True, bottom=True, labeltop=True, labelbottom=False)
        if args_im['label_orientation']=='below':
            ax.tick_params(top=True, bottom=True, labeltop=False, labelbottom=True)
        # Rotate the tick labels and set their alignment.
        # plt.setp(ax.get_xticklabels(), rotation=args_im['xtickRot'], ha="right", rotation_mode="anchor")
        ax.set_xticklabels(col_labels, rotation=args_im['xtickRot'], ha='center', minor=False)

    if not row_labels is None:
        ax.set_yticks(np.arange(data.shape[0]))
        ax.set_yticklabels(row_labels)
        ax.set_yticklabels(row_labels, rotation=args_im['ytickRot'], ha='right', minor=False)

    # Turn spines off and create white grid.
    # for edge, spine in ax.spines.items():
    #     spine.set_visible(False)

    if args_im['grid']:
        # if not col_labels is None:
        ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
        # if not row_labels is None:
        ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    if args_im['linewidth']>0 and args_im['grid']:
        ax.grid(which="minor", color=args_im['linecolor'], linestyle='-', linewidth=args_im['linewidth'])
    if args_im['axis']==False:
        plt.axis('off')
    ax.grid(False)

    return(im)


#%% Set defaults
def _defaults(args):
    # Extract the below for internal stuff
    getdefaults={'xlabel':None,'ylabel':None,'title':None,'axis':True,'grid':True,'normalize':False,'label_orientation':'below','verbose':3,'xtickRot':90,'ytickRot':0,'dpi':100,'figsize':(15,5)}
    args_im=dict()
    for getdefault in getdefaults:
        args_im.setdefault(getdefault, args.get(getdefault,getdefaults.get(getdefault)))
        try:
            args.pop(getdefault)
        except:
            pass
                
    # Set defaults for args
    args.setdefault('standard_scale', args.get('standard_scale',False))
    args.setdefault('cbar',True)
    args.setdefault('linewidth',0.1)
    args.setdefault('annot',False)
    args.setdefault('linecolor','#000000')
    args.setdefault('cmap','coolwarm')
    args.setdefault('vmin',None)
    args.setdefault('vmax',None)
    args.setdefault('distance','euclidean')
    args.setdefault('linkage','ward')
    # Return
    return(args, args_im)

# %% Check input
def _check_input(data, linewidth, args_im):
    # Must be >0
    if linewidth<0: linewidth=0
    # Check cols and rows with linewidth
    if ((data.shape[0]>100) or (data.shape[1]>100)) and (linewidth>0):
        if args_im['verbose']>=2: print('[IMAGESC] WARNING: Plot will be poorly visible if [linewidth>0] with rows/columns>100. Set linewidth=0 to adjust. [auto-adjusting...]' )
        linewidth=0
    
    return(linewidth)

# %% Check input
def _normalize(data, args_im):
    if args_im['normalize']:
        if args_im['verbose'] >=3: print('[IMAGESC] Normalzing data..')
        data = (data - data.mean()) / (data.max() - data.min())
    return(data)

# %%
def set_labels(data_shape, row_labels, col_labels):
    if row_labels is None:
        row_labels = np.arange(0, data_shape[0])
    if col_labels is None:
        col_labels = np.arange(0, data_shape[1])
    return(row_labels, col_labels)

# %%
def _annotate_heatmap(im, data=None, valfmt="{x:.2f}", textcolors=["black", "white"], threshold=None, **textkw):
    """Function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A list or array of two color specifications.  The first is used for
        values below a threshold, the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts
