import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Initialize the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

def load_html_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
sources = {'eu': 'https://visitors-centre.jrc.ec.europa.eu/en/media/tools/how-power-generated-europe-check-out-our-power-plant-database',
           'pypsa': 'https://github.com/PyPSA/powerplantmatching/tree/master'}

# Define the layout of the app
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H3("Comparing Europe Power Plant Datasets", 
                        style={'color': '#FFFFFF'}), width=12)
    ]),
    dbc.Row([  # Dropdowns row
        dbc.Col(dbc.Select(
            id='dropdown-1',
            options=[
                {'label': 'European Commission', 'value': 'eu'},
                {'label': 'PyPSA', 'value': 'pypsa'}
            ],
            value='eu',
            className="mb-2",
            style={
                    'border': '3px solid #ffbf00',  # Example: 2px wide green border
                    'border-radius': '5px',  # Optional: rounded corners
                }
        ), width=6, lg=2),  # Full width on small screens, 1/4th on large screens
        dbc.Col(dbc.Select(
            id='dropdown-2',
            options=[
                {'label': 'Count', 'value': 'count'},
                {'label': 'Power', 'value': 'power'}
            ],
            value='count',  # Default value for the second dropdown
            className="mb-2",  # Add some bottom margin for spacing
            style={
                    'border': '3px solid #ffbf00',  # Example: 2px wide green border
                    'border-radius': '5px',  # Optional: rounded corners
                }
        ), width=6, lg=2)  # Full width on small screens, 1/4th on large screens
    ]),
    dbc.Row([  # Iframe row
        dbc.Col(html.Iframe(id='central-html', 
                            style={"height": "570px", 
                                   "width": "870px",
                                   "border": "3px solid #ffbf00"}), width=12, lg=7),
        dbc.Col(html.Iframe(id='sub-html-image', 
                            style={"height": "422px", 
                                   "width": "100%",
                                   "border": "3px solid #ffbf00"}), width=12, lg=5)
    ]), 
    dbc.Row([
        dbc.Col(html.P([
                        "Source: ",
                        html.A(id='source-text', href="http://your-source-link.com", target="_blank", className="text-white")
                        ], className="text-center"), width=12)
    ], justify="center", className="mt-3"),
], fluid=True, style={'backgroundColor': '#191919'})

# Callback for updating the central HTML
@app.callback(
    [Output('central-html', 'src'), Output('source-text', 'children')],
    [Input('dropdown-1', 'value')]
)
def update_central_html(v1):
    s =  [
           html.A(sources[v1], href=sources[v1], target="_blank", className="text-white")
        ]
    return f'assets/{v1}.html', s

# Callback for updating the sub HTML image
@app.callback(
    Output('sub-html-image', 'src'),
    [Input('dropdown-1', 'value'),
     Input('dropdown-2', 'value'),]
)
def update_sub_html_image(v1, v2):
    return f'assets/{v1}_{v2}.html'


def update_source_link(selected_source):
    return 

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)