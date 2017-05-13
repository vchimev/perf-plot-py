import pandas as pd

df = pd.read_csv('perf_info.csv')
data = df['Launch'].tail(15) # Returns last n rows
plot = data.plot(title='Start Time')
fig = plot.get_figure()
fig.savefig('perf_info.png')

