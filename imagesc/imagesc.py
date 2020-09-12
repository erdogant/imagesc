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

"""
# --------------------------------------------------------------------------
# Name        : imagesc.py
# Author      : E.Taskesen
# Mail        : erdogant@gmail.com
# Licence     : MIT
# --------------------------------------------------------------------------

# %% Libraries
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from packaging import version
import os
from imagesc.utils.adjmat_vec import adjmat2vec
from shutil import copyfile
import webbrowser
import tempfile
curpath = os.path.dirname(os.path.abspath(__file__))


# %%
def d3(df, path=None, title='d3 Heatmap!', description='Heatmap description', width=500, height=500, fontsize=10, cmap='interpolateInferno', scale=False, vmin=None, vmax=None, showfig=True, stroke='red', verbose=3):
    """Heatmap in d3 javascript.

    Parameters
    ----------
    df : pd.DataFrame()
        Input data. The index and column names are used for the row/column naming.
    path : String, (Default: user temp directory)
        Directory path to save the output, such as 'c://temp/index.html'
    title : String, (default: 'd3 Heatmap!')
        Title text.
    description : String, (default: 'Heatmap description')
        Description text of the heatmap.
    width : int, (default: 500).
        Width of the window.
    height : int, (default: 500).
        height of the window.
    fontsize : int, (default: 10).
        Font size for the X and Y labels.
    scale : Bool, (default: True).
        Scale the values between [0-100].
    vmin : Bool, (default: 0).
        Range of colors starting with minimum value.
            * 1 : cells with value <1 are coloured white.
            * None : cells are colored based on the minimum value in the input data.
    vmax : Bool, (default: 100).
        Range of colors starting with maximum value.
            * 100 : cells above value >100 are capped.
            * None : cells are colored based on the maximum value in the input data.
    stroke : String, (default: 'red').
        Color of the recangle when hovering over a cell.
            * 'red'
            * 'black'
    showfig : Bool, (default: True)
        Open browser with heatmap.
    cmap : String, (default: 'interpolateInferno').
        The colormap scheme. This can be found at: https://github.com/d3/d3-scale-chromatic.
        Categorical:
            * 'schemeCategory10'
            * 'schemeAccent'
            * 'schemeDark2'
            * 'schemePaired'
            * 'schemePastel1'
            * 'schemePastel2'
            * 'schemeSet1'
            * 'schemeSet2'
            * 'schemeSet3'
            * 'schemeTableau10'
        Diverging:
            * 'interpolateInferno'
            * 'interpolatePRGn'
            * 'interpolatePiYG'
            * 'interpolatePuOr'
            * 'interpolateRdBu'
            * 'interpolateRdGy'
            * 'interpolateRdYlBu'
            * 'interpolateRdYlGn'
            * 'interpolateSpectral'
        Single color:
            * 'interpolateBlues'
            * 'interpolateGreens'
            * 'interpolateGreys'
            * 'interpolateOranges'
            * 'interpolatePurples'
            * 'interpolateReds'
        Sequential:
            * 'interpolateTurbo'
            * 'interpolateViridis'
            * 'interpolateInferno'
            * 'interpolateMagma'
            * 'interpolatePlasma'
            * 'interpolateCividis'
            * 'interpolateWarm'
            * 'interpolateCool'
            * 'interpolateCubehelixDefault'
            * 'interpolateBuGn'
            * 'interpolateBuPu'
            * 'interpolateGnBu'
            * 'interpolateOrRd'
            * 'interpolatePuBuGn'
            * 'interpolatePuBu'
            * 'interpolatePuRd'
            * 'interpolateRdPu'
            * 'interpolateYlGnBu'
            * 'interpolateYlGn'
            * 'interpolateYlOrBr'
            * 'interpolateYlOrRd'
        Cyclic:
            * 'interpolateRainbow'
            * 'interpolateSinebow'
    verbose : int [0-5], (default: 3)
        Verbosity to print the working-status. The higher the number, the more information.
            * 0: None
            * 1: Error
            * 2: Warning
            * 3: Info
            * 4: Debug
            * 5: Trace

    Example
    -------
    >>> import imagesc
    >>> df = pd.DataFrame(np.random.randint(0, 10, size=(7, 52)))
    >>> paths = imagesc.d3(df, fontsize=10, title='Python to d3 conversion!', description='Click here for the interactive website!', path='d3heatmap.html', height=200, width=750, cmap='interpolateGreens')

    Returns
    -------
    out : dict.
        output path names.

    """
    if cmap in ['schemeCategory10', 'schemeAccent', 'schemeDark2', 'schemePaired', 'schemePastel2', 'schemePastel1', 'schemeSet1', 'schemeSet2', 'schemeSet3', 'schemeTableau10']:
        cmap_type='scaleOrdinal'
        if verbose>=3: print('[imagesc] >d3 cmap type is set to %s' %(cmap_type))
    else:
        cmap_type='scaleSequential'

    # Rescale data between 0-100
    if scale:
        df = _scale(df, verbose=verbose)
    if (not scale) and (vmin is not None) and (vmax is not None):
        if verbose>=3: print('[imagesc] >Data is not scaled. Tip: set vmin=None and vmax=None to range colors between min-max of your data.')
    if vmin is None:
        vmin = np.min(df.values)
    if vmax is None:
        vmax = np.max(df.values)
    if verbose>=3: print('[imagesc] >vmin is set to: %g' %(vmin))
    if verbose>=3: print('[imagesc] >vmax is set to: %g' %(vmax))

    # Get path to files
    d3_library = os.path.abspath(os.path.join(curpath, 'd3js/d3.v4.js'))
    d3_chromatic = os.path.abspath(os.path.join(curpath, 'd3js/d3.scale.chromatic.v1.min.js'))
    d3_script = os.path.abspath(os.path.join(curpath, 'd3js/d3script.html'))

    # Set fontsize for x-axis, y-axis
    fontsize_x = fontsize
    fontsize_y = fontsize

    # Check path
    filename, dirpath, path = _path_check(path, verbose)

    # Copy files to destination directory
    copyfile(d3_library, os.path.join(dirpath, os.path.basename(d3_library)))
    copyfile(d3_chromatic, os.path.join(dirpath, os.path.basename(d3_chromatic)))
    copyfile(d3_script, path)

    # Convert into adj into vector
    dfvec = adjmat2vec(df)
    dfvec = dfvec.rename(columns={'source': 'variable', 'target': 'group', 'weight': 'value'})

    # Write to disk (file is not used)
    basename, ext = os.path.splitext(filename)
    PATHNAME_TO_CSV = os.path.join(dirpath, basename + '.csv')
    dfvec.to_csv(PATHNAME_TO_CSV, index=False)

    # Embed the Data in the HTML. Note that the embedding is an important stap te prevent security issues by the browsers.
    # Most (if not all) browser do not accept to read a file using d3.csv or so. It then requires security-by-passes, but thats not the way to go.
    # An alternative is use local-host and CORS but then the approach is not user-friendly coz setting up this, is not so straightforward.
    # It leaves us by embedding the data in the HTML. Thats what we are going to do here.
    DATA_STR = ''
    for i in range(0, dfvec.shape[0]):
        newline = '{group : "' + str(dfvec['group'].iloc[i]) + '", variable : "' + str(dfvec['variable'].iloc[i]) + '", value : "' + str(dfvec['value'].iloc[i]) +'"},'
        newline = newline + '\n'
        DATA_STR = DATA_STR + newline

    # Read the data
    # var data =
    # 	[
    # 		{"group":"A", "variable":"v1", "value":"3"},
    # 		{"group":"A", "variable":"v2", "value":"5"},
    # 		{"group":"B", "variable":"v1", "value":"10"},
    # 		{"group":"B", "variable":"v2", "value":"10"}
    # 	]

    # Import in the file
    with open(path, 'r') as file: d3graphscript = file.read()

    # Read the d3 html with script file
    d3graphscript = d3graphscript.replace('$DESCRIPTION$', str(description))
    d3graphscript = d3graphscript.replace('$TITLE$', str(title))

    d3graphscript = d3graphscript.replace('$WIDTH$', str(width))
    d3graphscript = d3graphscript.replace('$HEIGHT$', str(height))

    d3graphscript = d3graphscript.replace('$VMIN$', str(vmin))
    d3graphscript = d3graphscript.replace('$VMAX$', str(vmax))

    d3graphscript = d3graphscript.replace('$FONTSIZE_X$', str(fontsize_x))
    d3graphscript = d3graphscript.replace('$FONTSIZE_Y$', str(fontsize_y))

    d3graphscript = d3graphscript.replace('$STROKE$', str(stroke))
    d3graphscript = d3graphscript.replace('$CMAP$', str(cmap))
    d3graphscript = d3graphscript.replace('$CMAP_TYPE$', str(cmap_type))

    d3graphscript = d3graphscript.replace('$DATA_PATH$', filename)
    d3graphscript = d3graphscript.replace('$DATA_COMES_HERE$', DATA_STR)

    # Write to file
    with open(path, 'w') as file: file.write(d3graphscript)
    # Open browser with heatmap
    if showfig: webbrowser.open(path, new=1)
    # Return
    out = {}
    out['filename'] = filename
    out['dirpath'] = dirpath
    out['path'] = path
    out['csv'] = PATHNAME_TO_CSV
    return out


# %%
def plot(data, row_labels=None, col_labels=None, **args):
    """Heatmap plot.

    Parameters
    ----------
    data : numpy array
        data array.
    row_labels : List
        A list or array of length N with the labels for the rows.
    col_labels : List
        A list or array of length M with the labels for the columns.
    **args
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
    # sns.set_style({"savefig.dpi": args_im['dpi']})
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
    if args_im['label_orientation'] == 'above':
        ax.xaxis.tick_top()

    # Rotate labels
    ax.set_xticklabels(col_labels, rotation=args_im['xtickRot'], ha='center', minor=False)
    ax.set_yticklabels(row_labels, rotation=args_im['ytickRot'], ha='right', minor=False)
    # set the x-axis labels on the top
    
    # # fix for mpl bug that cuts off top/bottom of seaborn viz
    # b, t = plt.ylim() # discover the values for bottom and top
    # b += 0.5 # Add 0.5 to the bottom
    # t -= 0.5 # Subtract 0.5 from the top
    # plt.ylim(b, t) # update the ylim(bottom, top) values
    
    # Plot
    # ax.tight_layout()
    plt.show()
    # Return
    fig = ax.get_figure()
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
    plt.setp(g.ax_heatmap.get_yticklabels(), rotation=args_im['ytickRot'], ha='left')
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
    # Version check
    if not version.parse(matplotlib.__version__) > version.parse("3.1.1"):
        print('[IMAGESC] Warning: Matplotlib version is advised to be to be > v3.1.1. Otherwise heatmaps can have cut-off tops and bottoms.\nTry to: pip install -U matplotlib')

    # Extract the below for internal stuff
    getdefaults={'xlabel':None,'ylabel':None,'title':None,'axis':True,'grid':True,'normalize':False,'label_orientation':'below','verbose':3,'xtickRot':90,'ytickRot':0,'dpi':100,'figsize':(15,5)}
    args_im=dict()
    for getdefault in getdefaults:
        args_im.setdefault(getdefault, args.get(getdefault,getdefaults.get(getdefault)))
        try:
            args.pop(getdefault)
        except:
            pass
                
    # Set defaults for args that are feeded into the various baseline functions (seaborn, clustermap, imshow)
    args.setdefault('standard_scale', args.get('standard_scale',None))
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

# %% Adjust figure size based on input
def _set_figsize(data_shape, figsize):
    data_ratio = np.minimum(5/(data_shape[0]/data_shape[1]), 50)
    out = tuple(np.ceil(np.interp(data_shape-np.min(data_shape), [np.min(figsize), data_ratio], [np.max(figsize), data_ratio])))
    return(out[0], out[1])

# %%
def _path_check(path, verbose):
    # Check wether path
    if path is None:
        path = os.path.join(tempfile.gettempdir(), 'index.html')
    # Check wether dir + path
    dirpath, filename = os.path.split(path)
    # if input is single file, attach the absolute path.
    if dirpath=='':
        path = os.path.join(tempfile.gettempdir(), filename)
        dirpath, filename = os.path.split(path)
    # Check before proceeding
    if (not '.html' in filename):
        raise ValueError('[imagesc] >path should contain the file extension: ".html" ')
    # Create dir
    if not os.path.isdir(dirpath):
        if verbose>=2: print('[imagesc] >Warning: Creating directory [%s]' %(dirpath))
        os.makedirs(dirpath, exist_ok=True)
    # Final
    path = os.path.abspath(path)
    dirpath, filename = os.path.split(path)
    return filename, dirpath, path


# %% Scaling
def _scale(X, verbose=3):
    """Scale data.

    Description
    -----------
    Scaling in range by X*(100/max(X))

    Parameters
    ----------
    X : array-like
        Input image data.
    verbose : int (default : 3)
        Print to screen. 0: None, 1: Error, 2: Warning, 3: Info, 4: Debug, 5: Trace.

    Returns
    -------
    df : array-like
        Scaled image.

    """
    if verbose>=3: print('[imagesc] >Scaling image between [min-100]')
    try:
        # Normalizing between 0-100
        # X = X - X.min()
        X = X / X.max().max()
        X = X * 100
        X = np.round(X)
    except:
        if verbose>=2: print('[imagesc] >Warning: Scaling not possible.')

    return X


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
