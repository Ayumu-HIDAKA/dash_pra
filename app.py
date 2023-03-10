import dash
import dash_core_components as dcc
import dash_html_components as html
import sqlite3
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

table_name = 'iris'
conn = sqlite3.connect('db.sqlite')
df = pd.read_sql("select * from iris", conn) # irisデータのよみこみ



app.layout = html.Div(children=[

    html.H1(children='Hello Dash'),
    html.Div(children='Dash: A web application framework for Python.'),
    dcc.Graph(
        id='iris-graph',
        figure={
            'data': [
                dict(
                    x=df[df['target'] == i]['sepal_length_cm'],
                    y=df[df['target'] == i]['sepal_width_cm'],
                    text=df[df['target'] == i]['target'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.target.unique() # irisのカテゴリーごとにデータをとりだす
            ],
            'layout': dict( # グラフの色々な調整
                xaxis={'type': 'log', 'title': 'sepal_length'},
                yaxis={'title': 'sepal_width'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=5050, debug=True)