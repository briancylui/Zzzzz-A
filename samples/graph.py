import plotly.plotly as py
import plotly.graph_objs as go

py.sign_in('leoncheng57', 'j4xj7i52t2')

# Create random data with numpy
import numpy as np

drowsiness_history = [ [0,0,1,0], [1,1,1,1], [0,1,1,0], [1,1,0,0] ]

stat1 = []
stat2 = []
# stat3 = []
# stat4 = []
t = []
for x in drowsiness_history:
    stat1.append(x.count(0))
    stat2.append(x.count(1))
    # stat3.append(x[2])
    # stat4.append(x[3])
    t.append(len(t))

# t = [0,1,2,3,4,5,6]
# stat1 = [6,8,2,5,6,33,6]
# stat2 = [4,1,2,6,8,3,43]
# stat3 = [6,2,1,8,0,3,12]
# stat4 = [3,5,1,3,7,32,1]

# Create a trace
trace1 = go.Scatter(
    x = t,
    y = stat1
)

trace2 = go.Scatter(
    x = t,
    y = stat2
)

# trace3 = go.Scatter(
#     x = t,
#     y = stat3
# )

# trace4 = go.Scatter(
#     x = t,
#     y = stat4
# )

data = [trace1, trace2]

# Plot and embed in ipython notebook!
py.iplot(data, filename='basic-line')

