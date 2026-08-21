# CS4503 – Data Analytics and Visualization (Lab Manual)

Chennai Institute of Technology (Autonomous)
Course: CS4503 – Data Analytics and Visualization

This repository contains all the Python programs and their corresponding
outputs for the CS4503 lab manual, organized so that every experiment's
**code** and **output** are kept in separate top-level folders.

## Repository Structure

```
CS4503_DAV_Lab/
├── Program/     -> all .py source files (one per experiment)
├── Output/      -> one sub-folder per experiment with output.txt / screenshots / plots
├── .gitignore
└── README.md
```

## Experiment Index

| # | Program File | Output Folder | Description |
|---|---------------|----------------|-------------|
| 1 | `01_Installation_and_Exploration.py` | `01_Installation_and_Exploration/` | Install & explore NumPy, SciPy, Jupyter, Statsmodels, Pandas, Matplotlib, Seaborn, Plotly, Bokeh |
| 2A | `02A_NumPy_Arrays.py` | `02A_NumPy_Arrays/` | NumPy array creation, indexing, slicing, aggregation, structured arrays |
| 2B | `02B_Pandas_DataFrame.py` | `02B_Pandas_DataFrame/` | Pandas DataFrame operations: load, inspect, clean, filter, group, sort |
| 2C | `02C_Reading_Data_Text_Excel_Web.py` | `02C_Reading_Data_Text_Excel_Web/` | Reading data from CSV, Excel and web sources |
| 2D | `02D_Iris_Descriptive_Analytics.py` | `02D_Iris_Descriptive_Analytics/` | Descriptive analytics on the Iris dataset (histograms, boxplot, pairplot) |
| 3A | `03A_Univariate_Analysis.py` | `03A_Univariate_Analysis/` | Univariate statistics (mean, median, mode, variance, skewness, kurtosis) on UCI & Pima diabetes datasets |
| 3B | `03B_Bivariate_Regression.py` | `03B_Bivariate_Regression/` | Bivariate analysis using Linear & Logistic Regression |
| 3C | `03C_Multiple_Regression.py` | `03C_Multiple_Regression/` | Multiple regression predicting BMI |
| 3D | `03D_Comparison_Analysis.py` | `03D_Comparison_Analysis/` | Comparison of UCI vs Pima analysis results |
| 4A | `04A_Normal_Curves.py` | `04A_Normal_Curves/` | Normal curve visualization for Glucose & BMI |
| 4B | `04B_Z_Test.py` | `04B_Z_Test/` | Z-Test hypothesis testing on Glucose levels |
| 4C | `04C_T_Test.py` | `04C_T_Test/` | Independent T-Test between UCI and Pima datasets |
| 4D | `04D_ANOVA.py` | `04D_ANOVA/` | One-way ANOVA between UCI and Pima datasets |
| 5A | `05A_Linear_Models.py` | `05A_Linear_Models/` | Building & validating Linear Regression models |
| 5B | `05B_Logistic_Models.py` | `05B_Logistic_Models/` | Building & validating Logistic Regression models (with confusion matrices) |
| 5C | `05C_Time_Series_Analysis.py` | `05C_Time_Series_Analysis/` | Time series decomposition, moving average & ARIMA forecasting |

## Datasets Used

- **Iris dataset** (`iris_dataset(2d).csv`)
- **UCI Diabetes dataset** (`uci_diabetes.csv`)
- **Pima Indians Diabetes dataset** (`pima_diabetes.csv`)
- Sample CSV / Excel files for Experiments 2B & 2C (Google Play Store data, product/country lists)

> Dataset files are **not included** in this repository (see `.gitignore`).
> Place the required `.csv` / `.xlsx` files in the same directory as the
> script (or update the file paths inside each script) before running.

## Requirements

- Python 3.13.2
- Jupyter Notebook 7.3.2
- Packages: `numpy`, `scipy`, `pandas`, `matplotlib`, `seaborn`, `plotly`,
  `bokeh`, `statsmodels`, `scikit-learn`

Install everything with:

```bash
pip install numpy scipy jupyter statsmodels pandas matplotlib seaborn plotly bokeh scikit-learn
```

## How to Run

1. Open the desired script from the `Program/` folder in Jupyter Notebook / VS Code.
2. Ensure the dataset referenced in the script is present in the working directory.
3. Run the script/cells; generated plots will display inline (Jupyter) or in a
   pop-up window (script mode).
4. Compare your results with the reference output in the matching
   `Output/<experiment>/` folder.

## Notes

- Each `Output/<experiment>/` folder contains an `output.txt` with the console
  output (tables, statistics, scores) and, where the experiment produces a
  chart, the corresponding plot image(s)/screenshot(s).
- Results (R² scores, accuracy, p-values, etc.) may vary slightly between
  runs/machines depending on library versions and `random_state`/data splits.
