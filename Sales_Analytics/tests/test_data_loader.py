# tests/test_data_loader.py
import pandas as pd

from data_loader import DataLoader


def test_load_data(tmp_path):
    """
    DataLoader.load_data should read a CSV into a DataFrame
    and store it in the instance.
    """
    # Create temp CSV
    csv_path = tmp_path / "test_sales.csv"
    df = pd.DataFrame({"A": [1, 2, 3]})
    df.to_csv(csv_path, index=False)

    loader = DataLoader(str(csv_path))
    loaded = loader.load_data()

    assert isinstance(loaded, pd.DataFrame)
    assert len(loaded) == 3
    assert "A" in loaded.columns


def test_clean_data_drops_nulls_and_duplicates():
    df = pd.DataFrame(
        {
            "A": [1, 1, None],
            "B": [2, 2, 3],
        }
    )

    cleaned = DataLoader.clean_data(df)

    # Row with None should be dropped, one duplicate removed
    assert len(cleaned) == 1
    assert cleaned.iloc[0]["A"] == 1
    assert cleaned.iloc[0]["B"] == 2


def test_parse_dates_converts_columns_to_datetime():
    df = pd.DataFrame(
        {
            "Order Date": ["2015-01-01", "invalid"],
            "Ship Date": ["2015-01-02", "2015-01-03"],
        }
    )

    parsed = DataLoader.parse_dates(df)

    assert pd.api.types.is_datetime64_any_dtype(parsed["Order Date"])
    assert pd.api.types.is_datetime64_any_dtype(parsed["Ship Date"])
    # invalid should be coerced to NaT
    assert parsed["Order Date"].isna().sum() == 1


def test_add_calculated_fields_creates_expected_columns(raw_sales_df):
    df = DataLoader.parse_dates(raw_sales_df)
    df = DataLoader.add_calculated_fields(df)

    for col in ["Profit Margin", "Processing Days", "Revenue Per Unit", "Year", "Month", "Year-Month"]:
        assert col in df.columns

    # Check a couple of concrete values for first row
    first = df.iloc[0]
    # Profit Margin = Profit / Revenue * 100
    expected_margin = (first["Total Profit"] / first["Total Revenue"]) * 100
    assert round(first["Profit Margin"], 4) == round(expected_margin, 4)

    # Processing Days = Ship Date - Order Date
    assert first["Processing Days"] == (first["Ship Date"] - first["Order Date"]).days

    # Revenue Per Unit = Total Revenue / Units Sold
    expected_rpu = first["Total Revenue"] / first["Units Sold"]
    assert round(first["Revenue Per Unit"], 4) == round(expected_rpu, 4)


def test_get_info(transformed_sales_df):
    loader = DataLoader("dummy.csv")
    loader.data = transformed_sales_df

    info = loader.get_info()

    assert info["total_records"] == len(transformed_sales_df)
    assert "Region" in info["columns"]
    assert info["regions"] == transformed_sales_df["Region"].nunique()
    assert info["countries"] == transformed_sales_df["Country"].nunique()
    assert info["item_types"] == transformed_sales_df["Item Type"].nunique()
    assert "to" in info["date_range"]  # simple sanity check
