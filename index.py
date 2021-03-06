import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app, config, DWO
from apps import home
from apps import schema
#from apps import template
from apps import dim_municipio
from apps import fato_av_ppg
from apps import fato_rais

# Header
header = html.H3(#config['SITE']['HEADER'],
            style={"height":"62px",
                   "text-color":"white",
                   "background-image":"linear-gradient(#006600, #cccc00)",
                   "margin": "0",
                   "text-align":"center",
                   "font-family":"Verdana",
                   "font-size":"1.8em",
                   "font-weight":"100",
                   },
                className="align-middle text-white",
               )

# Navbar
navbar = dbc.NavbarSimple(
    children=[
        # Dcc Location
        dcc.Location(id='url', refresh=False),

        #dbc.NavLink("Template", href="/template"),
        dbc.NavLink("Schema", href="/schema"),
        # Dimensões
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("dim-municipio", href="/dim_municipio"),
            ],
            nav=True,
            in_navbar=True,
            label="Dimensões",
        ),
        # Economia
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("MTE", header=True),
                dbc.DropdownMenuItem("RAIS", href="/rais"),
                dbc.DropdownMenuItem("CAGED", href="#"),
                dbc.DropdownMenuItem("IBGE", header=True),
                dbc.DropdownMenuItem("IPCA", href="#"),
                dbc.DropdownMenuItem("INPC", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="Economia",
        ),
        # Educação
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("CAPES", header=True),
                dbc.DropdownMenuItem("Avaliação Pós", href="/fato_av_ppg"),
                dbc.DropdownMenuItem("MEC", header=True),
                dbc.DropdownMenuItem("Cursos de Graduação", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="Educação",
        ),
    ],
    brand = "Início",
    brand_href='/',
)

# Content
content = html.Div(id='page-content')

# Dash App's layout
app.title = config['SITE']['TITLE']

app.layout = html.Div([

    # Header
    dbc.Row(dbc.Col(header)
           ),

    # Navbar
    dbc.Row(dbc.Col(navbar),
           ),

    # Contents
    html.Div(id='page-content',
            ),

    ],

    style={"width":"80%", "margin":"0px auto", "padding-top":"20px",}
)

###############################################################################
# Callbacks
@app.callback(Output('page-content', 'children'),
                            [Input('url', 'pathname')])
def display_page(pathname):
    err= html.Div([html.P('Page not found!')])
    switcher = {
        '/': home.layout,
        '/dim_municipio': dim_municipio.layout,
        '/fato_av_ppg': fato_av_ppg.layout,
        '/rais': fato_rais.layout,
        '/schema': schema.layout,
        #'/template': template.layout,
    }
    return switcher.get(pathname, err)

###############################################################################
## Main
if __name__ == '__main__':

    if config['SITE']['DEBUG'] == "True":
        DEBUG=True
    else:
        DEBUG=False

    # Run Server
    app.run_server(host='0.0.0.0', debug=DEBUG)

