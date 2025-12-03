import pandas as pd
import operator
from data_loader import DataLoader
from stream_operations import StreamOperations
from sales_analytics import SalesAnalytics


def print_header(title: str):
    """Print formatted header."""
    print("\n" + "=" * 80)
    print(f" {title}")
    print("=" * 80)


def print_result(df: pd.DataFrame, title: str, rows: int = 10):
    """Print DataFrame results."""
    print(f"\n{title}")
    print("-" * 80)
    if len(df) == 0:
        print("No results found.")
    else:
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        print(df.head(rows).to_string(index=False))
        if len(df) > rows:
            print(f"... and {len(df) - rows} more rows")


def demo_stream_operations(data: pd.DataFrame):
    """Demonstrate stream operations."""
    print_header("STREAM OPERATIONS")
    
    stream = StreamOperations(data)
    
    # 1. Filter + Count
    print("\n1. Filter: High-value orders (Revenue > $100,000)")
    high_value_count = stream.filter(lambda x: x['Total Revenue'] > 100000).count()
    print(f"   Result: {high_value_count} orders found")
    
    # 2. Filter + Sorted + Limit
    print("\n2. Top 5 orders by profit (chained operations)")
    top_5 = (stream
             .filter(lambda x: x['Total Profit'] > 0)
             .sorted_by('Total Profit', ascending=False)
             .limit(5)
             .collect())
    print_result(top_5[['Order ID', 'Country', 'Item Type', 'Total Profit']], 
                 "   Top 5 Profitable Orders:", 5)
    
    # 3. Map operation
    print("\n3. Map: Extract profit margins")
    margins = stream.map(lambda x: x['Profit Margin'])
    print(f"   Average Margin: {margins.mean():.2f}%")
    print(f"   Max Margin: {margins.max():.2f}%")
    print(f"   Min Margin: {margins.min():.2f}%")
    
    # 4. Distinct values
    print("\n4. Distinct: Unique values")
    regions = stream.distinct('Region')
    channels = stream.distinct('Sales Channel')
    print(f"   Regions: {', '.join(regions)}")
    print(f"   Sales Channels: {', '.join(channels)}")
    
    # 5. Reduce operation
    print("\n5. Reduce: Calculate total revenue")
    total = stream.reduce_sum('Total Revenue')
    print(f"   Total Revenue: ${total:,.2f}")
    
    # 6. AnyMatch / AllMatch
    print("\n6. Match operations")
    has_loss = stream.any_match(lambda x: x['Total Profit'] < 0)
    all_positive = stream.all_match(lambda x: x['Total Revenue'] > 0)
    print(f"   Any loss-making orders? {has_loss}")
    print(f"   All orders have positive revenue? {all_positive}")
    
    # 7. Complex chain
    print("\n7. Complex chain: Online + High revenue + Top 3")
    complex_result = (stream
                      .filter(lambda x: x['Sales Channel'] == 'Online')
                      .filter(lambda x: x['Total Revenue'] > 50000)
                      .sorted_by('Total Profit', ascending=False)
                      .limit(3)
                      .collect())
    print_result(complex_result[['Order ID', 'Item Type', 'Total Revenue', 'Total Profit']], 
                 "   Result:", 3)
    
    # 8. Skip and Limit
    print("\n8. Skip first 10, take next 5 orders by revenue")
    skip_limit = (stream
                  .sorted_by('Total Revenue', ascending=False)
                  .skip(10)
                  .limit(5)
                  .collect())
    print_result(skip_limit[['Order ID', 'Country', 'Total Revenue']], 
                 "   Orders 11-15:", 5)


def demo_aggregations(data: pd.DataFrame):
    """Demonstrate aggregation operations."""
    print_header("AGGREGATION OPERATIONS")
    
    analytics = SalesAnalytics(data)
    
    # 1. Revenue by region
    print("\n1. Total Revenue by Region")
    result = analytics.total_revenue_by_region()
    print_result(result, "   Regional Performance:")
    
    # 2. Top countries
    print("\n2. Top 10 Countries by Revenue")
    result = analytics.top_countries_by_revenue(10)
    print_result(result, "   Top Countries:")
    
    # 3. Item type analysis
    print("\n3. Revenue by Item Type")
    result = analytics.revenue_by_item_type()
    print_result(result, "   Item Analysis:")
    
    # 4. Sales channel
    print("\n4. Sales Channel Comparison")
    result = analytics.sales_channel_comparison()
    print_result(result, "   Channel Performance:")
    
    # 5. Order priority
    print("\n5. Order Priority Analysis")
    result = analytics.order_priority_analysis()
    print_result(result, "   Priority Analysis:")
    
    # 6. Monthly trends
    print("\n6. Monthly Revenue Trend")
    result = analytics.monthly_revenue_trend()
    print_result(result, "   Monthly Trends:", 12)
    
    # 7. Top items by region
    print("\n7. Top 3 Profitable Items per Region")
    result = analytics.top_profitable_items_by_region(3)
    print_result(result, "   Regional Best Performers:", 15)
    
    # 8. Profit margins
    print("\n8. Top 10 Combinations by Profit Margin")
    result = analytics.profit_margin_by_category().head(10)
    print_result(result, "   High Margin Combinations:")


def demo_lambda_expressions(data: pd.DataFrame):
    """Demonstrate lambda expressions."""
    print_header("LAMBDA EXPRESSIONS")
    
    # 1. Filter with lambda
    print("\n1. Lambda filter: European orders over $50k")
    result = data[data.apply(
        lambda row: row['Region'] == 'Europe' and row['Total Revenue'] > 50000, 
        axis=1
    )]
    print(f"   Found {len(result)} orders")
    
    # 2. Map with lambda
    print("\n2. Lambda map: Calculate revenue per day")
    data['Revenue Per Day'] = data.apply(
        lambda row: row['Total Revenue'] / row['Processing Days'] 
        if row['Processing Days'] > 0 else 0, 
        axis=1
    )
    print(f"   Average revenue/day: ${data['Revenue Per Day'].mean():,.2f}")
    
    # 3. Sort with lambda key
    print("\n3. Lambda sort: Items by profit margin")
    result = (data.groupby('Item Type')['Profit Margin']
              .mean()
              .sort_values(ascending=False)
              .head(5))
    print("   Top 5 items by margin:")
    for item, margin in result.items():
        print(f"   - {item}: {margin:.2f}%")
    
    # 4. Complex lambda aggregation
    print("\n4. Lambda aggregation: Revenue statistics by region")
    result = data.groupby('Region').apply(
        lambda x: pd.Series({
            'Total Revenue': x['Total Revenue'].sum(),
            'Avg Order Value': x['Total Revenue'].mean(),
            'Max Order': x['Total Revenue'].max(),
            'Orders': len(x)
        })
    ).round(2)
    print_result(result.reset_index(), "   Statistics:")


def main():
    """Main entry point."""
    print("=" * 80)
    print(" SALES DATA ANALYSIS - FUNCTIONAL PROGRAMMING")
    print("=" * 80)
    csv_file = "/Users/padmajasharma/Desktop/Build Challenge/Sales_Analytics/sales_data.csv"

    
    try:
        # Load and transform data
        print("\nInitializing...")
        loader = DataLoader(csv_file)
        data = loader.load_data()
        
        # Apply transformations
        transformations = [
            DataLoader.clean_data,
            DataLoader.parse_dates,
            DataLoader.add_calculated_fields
        ]
        data = loader.apply_transformations(transformations)
        
        # Display info
        info = loader.get_info()
        print(f"\n✓ Dataset ready:")
        print(f"  - Total records: {info['total_records']}")
        print(f"  - Regions: {info['regions']}, Countries: {info['countries']}")
        print(f"  - Item types: {info['item_types']}")
        print(f"  - Date range: {info['date_range']}")
        
        # Run demonstrations
        demo_stream_operations(data)
        demo_aggregations(data)
        demo_lambda_expressions(data)
        
        print("\n" + "=" * 80)
        print(" ANALYSIS COMPLETE")
        print("=" * 80)
        
    except FileNotFoundError:
        print(f"\n✗ Error: File '{csv_file}' not found")
        print("\nPlease download sales data:")
        print("https://excelbianalytics.com/wp/wp-content/uploads/2017/07/10000-Sales-Records.zip")
        print("Extract and save as 'sales_data.csv' in the project directory")
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")


if __name__ == "__main__":
    main()