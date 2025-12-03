# tests/test_sales_analytics.py
import pandas as pd

from sales_analytics import SalesAnalytics
from data_loader import DataLoader


def test_total_revenue_by_region(transformed_sales_df):
    analytics = SalesAnalytics(transformed_sales_df)

    result = analytics.total_revenue_by_region()

    # Regions present
    assert set(result["Region"]) == set(transformed_sales_df["Region"].unique())

    # Sum matches original data
    region_sums = (
        transformed_sales_df.groupby("Region")["Total Revenue"].sum().reset_index()
    )
    merged = result.merge(region_sums, on="Region", suffixes=("", "_expected"))
    assert (merged["Total Revenue"] == merged["Total Revenue_expected"]).all()


def test_top_countries_by_revenue(transformed_sales_df):
    analytics = SalesAnalytics(transformed_sales_df)

    result = analytics.top_countries_by_revenue(n=2)

    assert len(result) == 2
    # Should be sorted descending by Total Revenue
    assert list(result["Total Revenue"]) == sorted(
        result["Total Revenue"], reverse=True
    )


def test_revenue_by_item_type(transformed_sales_df):
    analytics = SalesAnalytics(transformed_sales_df)

    result = analytics.revenue_by_item_type()

    # Multi-index columns like ("Total Revenue", "sum")
    assert "Item Type" in result.columns
    assert ("Total Revenue", "sum") in result.columns
    assert ("Total Profit", "sum") in result.columns

    # Check that sum over groups matches original total
    total_sum = transformed_sales_df["Total Revenue"].sum()
    grouped_sum = result[("Total Revenue", "sum")].sum()
    assert round(total_sum, 4) == round(grouped_sum, 4)


def test_sales_channel_comparison(transformed_sales_df):
    analytics = SalesAnalytics(transformed_sales_df)

    result = analytics.sales_channel_comparison()

    channels = set(result["Sales Channel"])
    expected_channels = set(transformed_sales_df["Sales Channel"].unique())
    assert channels == expected_channels

    # Column structure
    assert ("Total Revenue", "sum") in result.columns
    assert ("Total Profit", "sum") in result.columns


def test_order_priority_analysis(transformed_sales_df):
    analytics = SalesAnalytics(transformed_sales_df)

    result = analytics.order_priority_analysis()

    assert set(result["Order Priority"]) == set(
        transformed_sales_df["Order Priority"].unique()
    )
    # Ensure Processing Days mean is positive
    assert (result["Processing Days"] >= 0).all()


def test_monthly_revenue_trend(transformed_sales_df):
    analytics = SalesAnalytics(transformed_sales_df)

    result = analytics.monthly_revenue_trend()

    # Grouped by Year-Month
    assert "Year-Month" in result.columns
    assert ("Total Revenue", "sum") not in result.columns  # here it's flat columns?
    # They aggregate with simple dict, so columns are: Total Revenue, Total Profit, Order ID
    assert "Total Revenue" in result.columns
    assert len(result) == transformed_sales_df["Year-Month"].nunique()


def test_top_profitable_items_by_region(transformed_sales_df):
    analytics = SalesAnalytics(transformed_sales_df)

    result = analytics.top_profitable_items_by_region(n=2)

    # At most 2 per region
    counts = result.groupby("Region")["Item Type"].count()
    assert (counts <= 2).all()

    # Sorted within each region by Total Profit descending
    for region, group in result.groupby("Region"):
        profits = list(group["Total Profit"])
        assert profits == sorted(profits, reverse=True)


def test_profit_margin_by_category(transformed_sales_df):
    analytics = SalesAnalytics(transformed_sales_df)

    result = analytics.profit_margin_by_category()

    assert "Profit Margin" in result.columns
    # Sorted by Profit Margin descending
    margins = list(result["Profit Margin"])
    assert margins == sorted(margins, reverse=True)


def test_yearly_comparison(transformed_sales_df):
    analytics = SalesAnalytics(transformed_sales_df)

    result = analytics.yearly_comparison()

    years = set(result["Year"])
    expected_years = set(transformed_sales_df["Year"].unique())
    assert years == expected_years

    assert "Total Revenue" in result.columns
    assert "Total Profit" in result.columns
    assert "Profit Margin" in result.columns


def test_high_value_orders(transformed_sales_df):
    analytics = SalesAnalytics(transformed_sales_df)

    # Use a small threshold to ensure at least one match
    threshold = transformed_sales_df["Total Revenue"].min() + 1
    result = analytics.high_value_orders(threshold=threshold)

    assert len(result) > 0
    assert all(result["Total Revenue"] > threshold)


def test_low_margin_items(transformed_sales_df):
    analytics = SalesAnalytics(transformed_sales_df)

    # Use a high threshold to force some low-margin items (depending on synthetic data)
    result = analytics.low_margin_items(threshold=100)

    assert "Item Type" in result.columns
    assert "Profit Margin" in result.columns
    # All averages below threshold
    assert (result["Profit Margin"] < 100).all()


def test_custom_aggregation(transformed_sales_df):
    analytics = SalesAnalytics(transformed_sales_df)

    result = analytics.custom_aggregation(
        group_by=["Region"],
        agg_dict={"Total Revenue": "sum", "Total Profit": "sum"},
    )

    assert set(result["Region"]) == set(transformed_sales_df["Region"].unique())

    # Check sums match manual groupby
    manual = (
        transformed_sales_df.groupby("Region")[["Total Revenue", "Total Profit"]]
        .sum()
        .reset_index()
    )
    merged = result.merge(manual, on="Region", suffixes=("", "_expected"))

    assert (merged["Total Revenue"] == merged["Total Revenue_expected"]).all()
    assert (merged["Total Profit"] == merged["Total Profit_expected"]).all()
