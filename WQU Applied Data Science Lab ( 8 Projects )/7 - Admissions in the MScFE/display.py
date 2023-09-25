from business import GraphBuilder, StatsBuilder
from dash import Input, Output, State, dcc, html
from jupyter_dash import JupyterDash

# Task 7.4.1
app = ...
# Task 7.4.8
gb = ...
# Task 7.4.13
sb = ...

# Tasks 7.4.1, 7.4.2, 7.4.3, 7.4.11, 7.4.14, 7.4.16
app.layout = ...


# Tasks 7.4.4, 7.4.8, 7.4.9, 7.4.10

def display_demo_graph(graph_name):
    """Serves applicant demograhic visualization.

    Parameters
    ----------
    graph_name : str
        User input given via 'demo-plots-dropdown'. Name of Graph to be returned.
        Options are 'Nationality', 'Age', 'Education'.

    Returns
    -------
    dcc.Graph
        Plot that will be displayed in 'demo-plots-display' Div.
    """
    
    return dcc.Graph()


# Task 7.4.13

def display_group_size(effect_size):
    """Serves information about required group size.

    Parameters
    ----------
    effect_size : float
        Size of effect that user wants to detect. Provided via 'effect-size-slider'.

    Returns
    -------
    html.Div
        Text with information about required group size. will be displayed in
        'effect-size-display'.
    """
    
    return html.Div()


# Task 7.4.15

def display_cdf_pct(effect_size, days):
    """Serves probability of getting desired number of obervations.

    Parameters
    ----------
    effect_size : float
        The effect size that user wants to detect. Provided via 'effect-size-slider'.
    days : int
        Duration of the experiment. Provided via 'experiment-days-slider'.

    Returns
    -------
    html.Div
        Text with information about probabilty. Goes to 'experiment-days-display'.
    """
    # Calculate number of observations

    # Calculate percentage

    # Create text
    
    # Return Div with text
    return html.Div()


# Task 7.4.17

def display_results(n_clicks, days):
    """Serves results from experiment.

    Parameters
    ----------
    n_clicks : int
        Number of times 'start-experiment-button' button has been pressed.
    days : int
        Duration of the experiment. Provided via 'experiment-days-display'.

    Returns
    -------
    html.Div
        Experiment results. Goes to 'results-display'.
    """
    
    return html.Div()
