"""
A collections of functions to help when working with pyspark
"""

from __future__ import division

import numpy as np
from numpy import linspace

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import mlab


def categoricals_distribution(target_df, col_index, order_by_categ=False):
    """
    Plot two charts to represent the frequency a value occurs in the specified
    column of a specified dataframe
    """
    col_name = target_df.columns[col_index]
    col_rows = target_df.groupby(col_name).count().collect()
    col_list_unord = map(lambda x: (x.asDict()[col_name], x.asDict()['count']), col_rows)

    order_index = 0 if order_by_categ else 1
    col_count_list = sorted(col_list_unord, key=lambda y: y[order_index], reverse=False)

    # save the categories (distinct values) and their respective counts separately
    col_categs = zip(*col_count_list)[0]
    col_counts = zip(*col_count_list)[1]

    # Font configurations
    fontsize2use = 7
    title_font = fm.FontProperties(family='Bitstream Vera Sans', style='normal',
                                   size=18, weight='normal', stretch='normal')
    ticks_font = fm.FontProperties(family='Bitstream Vera Sans', style='normal',
                                   size=fontsize2use, weight='normal', stretch='normal')

    # FIRST CHART - Distribution
    ordered_col_counts = col_counts

    if order_by_categ:
        ordered_col_counts = sorted(col_counts)

    p = linspace(0.0, 100.0, 11)
    perc = mlab.prctile(ordered_col_counts, p=p)

    # Chart properties
    chart_title = '[{}] -> {} categs'.format(col_name, len(ordered_col_counts))

    fig = plt.figure(figsize=(20, 5))
    ax = fig.add_subplot(111)
    ax.set_title(chart_title, fontproperties=title_font)
    ax.set_ylabel('Calls')

    # Plot the line
    plt.plot(ordered_col_counts, color='b', alpha=0.4)

    # Place gray dots on the percentiles
    plt.plot(((len(ordered_col_counts) - 1) * p / 100.), perc, 'o', color='k', alpha=0.5)

    # Set tick locations and labels
    plt.xticks(((len(ordered_col_counts) - 1) * p / 100.), map(str, p))
    plt.show()

    # SECOND CHART - Frequency per Category
    fig_width = int(len(col_counts) // 4.8)
    fig_height = len(col_counts) // 15

    fig_width = 20 if (fig_width < 20) else fig_width
    fig_height = 5 if (fig_height < 5) else fig_height

    fig = plt.figure(figsize=(fig_width, fig_height))

    plt.xticks(fontsize=fontsize2use)
    plt.yticks(fontsize=fontsize2use)

    ax = fig.add_subplot(111)
    ax.set_ylabel('Calls')

    ax.set_xticks(map(lambda x: x, range(0, len(col_categs))))
    ax.set_xticklabels(col_categs, rotation=45, rotation_mode='anchor', ha='right',
                       fontproperties=ticks_font)

    ax.yaxis.grid(True)

    for label in ax.get_yticklabels():
        label.set_fontproperties(ticks_font)

    x_pos = np.arange(len(col_categs))

    plt.bar(x_pos, col_counts, align='center')
    plt.xticks(x_pos, col_categs)

    plt.show()
