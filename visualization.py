import plotly.graph_objects as go

def plot():
    fig = go.Figure()

    fig.add_trace( go.Line( x = [i for i in range(10)] , y = [ i*i for i in range(10) ] ) )

    return fig

def plotBar(x, y):
    fig = go.Figure()

    fig.add_trace( go.Bar( x = x , y = y ) )

    return fig

def plotLine(x, y):
    fig = go.Figure()

    fig.add_trace( go.Line( x = x , y = y ) )

    return fig