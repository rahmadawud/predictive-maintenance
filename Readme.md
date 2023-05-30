# Data-Driven Predictive Maintenance

This project is conducted as part of the Data Minining course at Constractor University (2023).

The goal of the project is developing a machine learning model for predicting machine failures due to a specific component within a 48(X)-hour time window. Leveraging the [Microsoft Azure Predictive Maintenance dataset](https://www.kaggle.com/datasets/arnabbiswas1/microsoft-azure-predictive-maintenance) and conducting exploratory data analysis, valuable insights and patterns have been uncovered. The feature engineering process incorporated lag features, maintenance history, and machine-specific features capturing relevant information for failure prediction.

We employed both Multi-Layer Perceptron (MLP) and LightGBM model for tackling the multi-class failure classification task. 

[Optuna](https://optuna.readthedocs.io/en/stable/index.html) is used for hyperparameter optimization. 


## Project Structure
```
├── data
│   ├── PdM_errors.csv
│   ├── PdM_failures.csv
│   ├── PdM_machines.csv
│   ├── PdM_maint.csv
│   ├── PdM_telemetry.csv
│   └── training_data.parquet
├── EDA.ipynb
├── Feature_engineering.ipynb
├── Modeling.ipynb
├── Predictive_maintenance.pptx
├── Readme.md
└── requirements.txt
└── report.docx
└── utils.py
```

- EDA.ipynb: Exploratory Data Analysis
- Feature_engineering.ipynb: Creates the features and the target variable and stores the training data under 'data/training_data.parquet'
- Modeling.ipynb: Trains and evaluates both MLP and LightGBM models
- report.doc: Project report
- requirements.txt: Project requirements
- utils.py: Contains the load_data function


## Usage

1. Install the requirements:
```
    pip install -r requirements.txt
```

2. Run the notebooks in the order

    EDA -> Feature_engineering -> Modeling