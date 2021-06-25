import plotly.graph_objects as go
import plotly.express as px


# -------------------------------------------Plot Pie Chart--------------------


def plotpie(labels, values, title, template):
    # color_continuous_scale='inferno'
    layout = go.Layout(title=title, template=template)
    fig = go.Figure(layout=layout)
    # for template in [ "ggplot2"]:
    # fig.update_layout(template=template)
    fig.add_trace(go.Pie(labels=labels, values=values, title='Genre', textinfo='label+percent', hole=0.2,
                         marker=dict(colors=['#f7d468', '#74cb35'],
                                     line_color='Gray',
                                     line_width=1),
                         textfont={'color': '#000', 'size': 12},
                         textfont_size=12))
    return fig

# --------------------------------Plot Bar Chart------------------------


def plotBar(x, y, title='Default Title', xlabel='xlabel', ylabel='ylabel'):
    #layout=go.Layout(title=go.layout.Title(text="Number of Fiction Book published per Year."), hovermode='closest',xaxis=dict(title='Number Of Books', type='log', autorange=True),yaxis=dict(title='Years', type='log', autorange=True))

    layout = go.Layout(title=title,
                       xaxis=dict(title=xlabel),
                       yaxis=dict(title=ylabel))
    fig = go.Figure(layout=layout)
    # fig.add_trace( go.Bar(x = x,y= y, marker = dict(color = ['#ff6666','#f76e6e', '#f07575', '#e87d7d', '#e08585',
    # '#d98c8c', '#d19494', '#c99c9c','#c2a3a3', '#baabab'], colors=['indianred', 'lightsalmon']
    # )))
    fig.add_trace(go.Bar(x=x, y=y))
    return fig

# -------------------------------Plot GroupBAR Chart-----------------------


def plotGroupedBar(datapoints, categories, title, xlabel, ylabel, colors=['indianred', 'lightsalmon']):
    #layout=go.Layout(title=go.layout.Title(text="Number of Fiction Book published per Year."), hovermode='closest',xaxis=dict(title='Number Of Books', type='log', autorange=True),yaxis=dict(title='Years', type='log', autorange=True))

    layout = go.Layout(title=title,
                       xaxis=dict(title=xlabel),
                       yaxis=dict(title=ylabel))
    fig = go.Figure(layout=layout)

    for category, point, color in zip(categories, datapoints, colors):
        fig.add_trace(go.Bar(x=point.index, y=point.values,
                             name=category, marker_color=color))

    return fig

# ------------------------------------------


def plotLine(datapoints, title='Default Title', xlabel='xlabel', ylabel='ylabel'):
    layout = go.Layout(title=title,
                       xaxis=dict(title=xlabel),
                       yaxis=dict(title=ylabel))
    fig = go.Figure(layout=layout)
    fig.add_trace(go.Line(x=datapoints.index,
                          y=datapoints.values, line_color='#f63366'))
    return fig


def plotMultiLine(datapoints, title, xlabel, ylabel, template="plotly_dark"):
    layout = go.Layout(title=title,
                       xaxis=dict(title=xlabel),
                       yaxis=dict(title=ylabel), template=template)
    fig = go.Figure(layout=layout)

    for datapoint in datapoints:
        fig.add_trace(go.Line(x=datapoint.get('x'),
                              y=datapoint.get('y'), line_color='#f63366'))
    return fig


# --------------------------------

def plotHistogram(datapoints, title, xlabel, ylabel):
    layout = go.Layout(title=title,
                       xaxis=dict(title=xlabel),
                       yaxis=dict(title=ylabel))
    fig = go.Figure(layout=layout)

    fig.update_layout(template="ggplot2")
    fig.add_trace(go.Histogram(
        x=datapoints.values,
        # xbins = {'start': 1, 'size': 0.1, 'end' : 5}
    ))

    return fig
