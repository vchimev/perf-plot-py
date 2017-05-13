import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

column = 'Launch'
timestamp = 'Timestamp'

df = pd.read_csv('perf_info.csv', nrows=15)
df.head()

trace = go.Scatter(
                   # Data
                   x=df[timestamp],
                   y=df[column],
                   # Additional options
                   # fill='tozeroy',
                   # mode='lines+markers',
                   name=column,
                   line=dict(
                             color=('rgb(205, 12, 24)'),
                             width=5
                            )
                  )

layout = go.Layout(title=column + " Plot",
                   plot_bgcolor='rgb(230, 230,230)')

fig = go.Figure(data=[trace], layout=layout)
py.image.save_as(fig, 'perf_info', format='png')

