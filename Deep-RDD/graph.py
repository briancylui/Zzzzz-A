import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

py.sign_in('leoncheng57', 'j4xj7i52t2')

drowsiness_history = [ [0,0,1,0], [1,1,1,1], [0,1,1,0], [1,1,0,0] ]

stat1 = []
stat2 = []
t = []
for x in drowsiness_history:
    stat1.append(x.count(0))
    stat2.append(x.count(1))
    t.append(len(t))

trace1 = go.Scatter(
    x = t,
    y = stat1
)

trace2 = go.Scatter(
    x = t,
    y = stat2
)

data = [trace1, trace2]

py.plot(data, filename='basic-line')


