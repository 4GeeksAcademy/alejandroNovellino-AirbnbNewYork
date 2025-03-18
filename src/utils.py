import os
import pandas as pd


def load_data(file_path: str, url: str) -> pd.DataFrame:
    """
    Loads data from a file if it exists, otherwise from a URL.

    Args:
        file_path (str): The path to the file.
        url (str): The URL to load data from if the file doesn't exist.

    Returns:
        pandas.DataFrame: The loaded DataFrame.

    Raise:
        Exception: if no data could be loaded
    """

    if os.path.exists(file_path):
        print(f"Loading data from file: {file_path}")
        df = pd.read_csv(file_path)

        return df
    else:
        print(f"File not found. Loading data from URL: {url}")

        try:

            df = pd.read_csv(url)
            # save the DataFrame to the file for future use
            df.to_csv(file_path)
            print(f"Data saved to file: {file_path}")

        except Exception as e:
            print(f"Error loading data from URL: {e}")
            raise Exception("Not data could be loaded.") from e

    return df
