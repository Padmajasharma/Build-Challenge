# tests/conftest.py
import pandas as pd
import pytest
from datetime import datetime

from data_loader import DataLoader


@pytest.fixture
def raw_sales_df():
    """
    Small synthetic sales dataset that mimics the real CSV schema.
    This is used as a base for many tests.
    """
    data = {
        "Region": ["Europe", "Europe", "Asia", "Asia"],
        "Country": ["France", "Germany", "India", "China"],
        "Item Type": ["Clothes", "Clothes", "Baby Food", "Clothes"],
        "Sales Channel": ["Online", "Offline", "Online", "Offline"],
        "Order Priority": ["H", "M", "L", "C"],
        "Order Date": [
            "2015-01-01",
            "2015-01-10",
            "2016-02-05",
            "2016-02-20",
        ],
        "Order ID": [1, 2, 3, 4],
        "Ship Date": [
            "2015-01-05",
            "2015-01-15",
            "2016-02-10",
            "2016-02-25",
        ],
        "Units Sold": [10, 20, 5, 15],
        "Unit Price": [5.0, 4.0, 30.0, 7.0],
        "Unit Cost": [3.0, 2.5, 20.0, 4.0],
    }

    df = pd.DataFrame(data)

    # Compute Total Revenue, Total Cost, Total Profit as CSV would have
    df["Total Revenue"] = df["Units Sold"] * df["Unit Price"]
    df["Total Cost"] = df["Units Sold"] * df["Unit Cost"]
    df["Total Profit"] = df["Total Revenue"] - df["Total Cost"]

    return df


@pytest.fixture
def transformed_sales_df(raw_sales_df):
    """
    Apply the same transformations that main.py uses:
    clean_data -> parse_dates -> add_calculated_fields
    """
    df = raw_sales_df.copy()
    df = DataLoader.clean_data(df)
    df = DataLoader.parse_dates(df)
    df = DataLoader.add_calculated_fields(df)
    return df
