# pylint: disable=C0103
"""
    This module:
        - reads a .csv file
        - creates a plot
        - saves it to a .png file
"""
import pandas as pd

df = pd.read_csv('perf_info.csv')
data = df[['Timestamp', 'Launch']].loc[df['Hostname']
                                       == 'mcsofnsbuild07'].tail(15)
plot = data.plot(x='Timestamp', y='Launch', legend=False,
                 linewidth=5, rot=23, title='Start Time')
fig = plot.get_figure()
fig.set_size_inches(10, 8)
fig.savefig('perf_info.png')
