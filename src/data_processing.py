import pandas as pd
import numpy as np

def load_raw_data(file_path):
    """
    Loads the raw data.

    Args:
        file_path (str): Path to the raw data file.

    Returns:
        pandas.DataFrame: The raw data.
    """

    df = pd.read_csv(file_path)
    return df