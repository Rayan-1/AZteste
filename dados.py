import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Conecte-se ao banco de dados SQLite
db_path = 'populacao.db'
engine = create_engine(f'sqlite:///{db_path}')

# Consulta SQL para obter os dados
consulta = "SELECT cidade, populacao FROM populacao"
df = pd.read_sql_query(consulta, engine)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1("População das Cidades do Ceará", style={'textAlign': 'center'}),
    
    dcc.Dropdown(
        id='cidade-dropdown',
        options=[{'label': cidade, 'value': cidade} for cidade in df['cidade']],
        value=df['cidade'][0],
        style={'width': '50%', 'margin': '0 auto'}
    ),
    
    dcc.Graph(
        id='populacao-grafico',
        config={'displayModeBar': False}  # Remover a barra de opções do gráfico
    ),
    
    html.Div(id='cidade-info', style={'textAlign': 'center', 'margin-top': '20px'})
])

@app.callback(
    [dash.dependencies.Output('populacao-grafico', 'figure'),
     dash.dependencies.Output('cidade-info', 'children')],
    [dash.dependencies.Input('cidade-dropdown', 'value')]
)
def atualizar_grafico(selected_cidade):
    filtered_df = df[df['cidade'] == selected_cidade]

    figura = {
        'data': [
            {'x': filtered_df['cidade'], 'y': filtered_df['populacao'], 'type': 'bar', 'name': 'População'},
        ],
        'layout': {
            'title': f'População de {selected_cidade}',
            'xaxis': {'title': 'Cidade'},
            'yaxis': {'title': 'População'},
        }
    }
    
    info = f"A população de {selected_cidade} é de {filtered_df['populacao'].values[0]:,} habitantes."
    
    return figura, info

if __name__ == '__main__':
    app.run_server(debug=True)
