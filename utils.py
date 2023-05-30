import pandas as pd


def load_data():
    """Load data from csv files

    Returns
    -------
    df_telemetry : pd.DataFrame 
        Telemetry data
    df_errors : pd.DataFrame
        Errors log
    df_maintenance : pd.DataFrame
        Maintenance log
    df_failures : pd.DataFrame
        Failure log
    df_machines : pd.DataFrame
        Machine meta data
    """
    
    df_telemetry = pd.read_csv("data/PdM_telemetry.csv")
    df_errors = pd.read_csv("data/PdM_errors.csv")
    df_maintenance = pd.read_csv("data/PdM_maint.csv")
    df_failures = pd.read_csv("data/PdM_failures.csv")
    df_machines = pd.read_csv("data/PdM_machines.csv")

    # Convert datetime string to datetime object
    df_telemetry["datetime"] = pd.to_datetime(
        df_telemetry["datetime"], format="%Y-%m-%d %H:%M:%S"
    )
    df_errors["datetime"] = pd.to_datetime(
        df_errors["datetime"], format="%Y-%m-%d %H:%M:%S"
    )
    df_maintenance["datetime"] = pd.to_datetime(
        df_maintenance["datetime"], format="%Y-%m-%d %H:%M:%S"
    )
    df_failures["datetime"] = pd.to_datetime(
        df_failures["datetime"], format="%Y-%m-%d %H:%M:%S"
    )

    return df_telemetry, df_errors, df_maintenance, df_failures, df_machines
