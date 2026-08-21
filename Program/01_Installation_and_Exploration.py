"""
Experiment 1: Download, install and explore the features of NumPy, SciPy,
Jupyter, Statsmodels, Pandas, Matplotlib, Seaborn, Plotly, and Bokeh.

AIM:
To download, install, and explore the features of NumPy, SciPy, Jupyter,
Statsmodels, Pandas, Matplotlib, Seaborn, Plotly, and Bokeh for scientific
computing, data analysis, and visualization.

Command Prompt:
pip install numpy scipy jupyter statsmodels pandas matplotlib seaborn plotly bokeh
"""

import numpy as np
print("NumPy Version:", np.__version__)

import pandas as pd
print("Pandas Version:", pd.__version__)

import matplotlib
print("Matplotlib Version:", matplotlib.__version__)

import seaborn as sns
print("Seaborn Version:", sns.__version__)

import statsmodels.api as sm
print("Statsmodels Version:", sm.__version__)

import scipy
print("SciPy Version:", scipy.__version__)

import plotly
print("Plotly Version:", plotly.__version__)

import bokeh
print("Bokeh Version:", bokeh.__version__)

import jupyterlab
print("JupyterLab Version:", jupyterlab.__version__)
