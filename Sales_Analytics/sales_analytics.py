import pandas as pd
from typing import List, Dict, Callable


class SalesAnalytics:
    """Performs various analytics on sales data."""
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize with sales data.
        
        Args:
            data: Sales DataFrame
        """
        self.data = data
    
    def total_revenue_by_region(self) -> pd.DataFrame:
        """Calculate total revenue by region."""
        return (self.data.groupby('Region')
                .agg({
                    'Total Revenue': 'sum',
                    'Total Profit': 'sum',
                    'Order ID': 'count'
                })
                .rename(columns={'Order ID': 'Orders'})
                .sort_values('Total Revenue', ascending=False)
                .reset_index())
    
    def top_countries_by_revenue(self, n: int = 10) -> pd.DataFrame:
        """Get top N countries by revenue."""
        return (self.data.groupby('Country')
                .agg({
                    'Total Revenue': 'sum',
                    'Total Profit': 'sum',
                    'Units Sold': 'sum'
                })
                .sort_values('Total Revenue', ascending=False)
                .head(n)
                .reset_index())
    
    def revenue_by_item_type(self) -> pd.DataFrame:
        """Analyze revenue by item type."""
        return (self.data.groupby('Item Type')
                .agg({
                    'Total Revenue': ['sum', 'mean', 'max'],
                    'Total Profit': ['sum', 'mean'],
                    'Units Sold': 'sum',
                    'Order ID': 'count'
                })
                .round(2)
                .sort_values(('Total Revenue', 'sum'), ascending=False)
                .reset_index())
    
    def sales_channel_comparison(self) -> pd.DataFrame:
        """Compare online vs offline sales."""
        return (self.data.groupby('Sales Channel')
                .agg({
                    'Total Revenue': ['sum', 'mean'],
                    'Total Profit': ['sum', 'mean'],
                    'Order ID': 'count',
                    'Profit Margin': 'mean'
                })
                .round(2)
                .reset_index())
    
    def order_priority_analysis(self) -> pd.DataFrame:
        """Analyze by order priority."""
        return (self.data.groupby('Order Priority')
                .agg({
                    'Total Revenue': 'sum',
                    'Total Profit': 'sum',
                    'Processing Days': 'mean',
                    'Order ID': 'count'
                })
                .round(2)
                .sort_values('Total Revenue', ascending=False)
                .reset_index())
    
    def monthly_revenue_trend(self) -> pd.DataFrame:
        """Calculate monthly revenue trends."""
        return (self.data.groupby('Year-Month')
                .agg({
                    'Total Revenue': 'sum',
                    'Total Profit': 'sum',
                    'Order ID': 'count'
                })
                .round(2)
                .reset_index())
    
    def top_profitable_items_by_region(self, n: int = 5) -> pd.DataFrame:
        """Get top N profitable items per region."""
        return (self.data.groupby(['Region', 'Item Type'])
                .agg({
                    'Total Profit': 'sum',
                    'Total Revenue': 'sum',
                    'Order ID': 'count'
                })
                .reset_index()
                .sort_values(['Region', 'Total Profit'], ascending=[True, False])
                .groupby('Region')
                .head(n)
                .reset_index(drop=True))
    
    def profit_margin_by_category(self) -> pd.DataFrame:
        """Analyze profit margins by different categories."""
        return (self.data.groupby(['Region', 'Item Type'])
                .agg({
                    'Profit Margin': 'mean',
                    'Total Revenue': 'sum',
                    'Total Profit': 'sum'
                })
                .round(2)
                .sort_values('Profit Margin', ascending=False)
                .reset_index())
    
    def yearly_comparison(self) -> pd.DataFrame:
        """Compare performance by year."""
        return (self.data.groupby('Year')
                .agg({
                    'Total Revenue': 'sum',
                    'Total Profit': 'sum',
                    'Order ID': 'count',
                    'Profit Margin': 'mean'
                })
                .round(2)
                .reset_index())
    
    def high_value_orders(self, threshold: float = 100000) -> pd.DataFrame:
        """Get high-value orders above threshold."""
        return (self.data[self.data['Total Revenue'] > threshold]
                .sort_values('Total Revenue', ascending=False)
                [['Order ID', 'Country', 'Item Type', 'Total Revenue', 'Total Profit']]
                .reset_index(drop=True))
    
    def low_margin_items(self, threshold: float = 10) -> pd.DataFrame:
        """Identify items with low profit margins."""
        return (self.data[self.data['Profit Margin'] < threshold]
                .groupby('Item Type')
                .agg({
                    'Profit Margin': 'mean',
                    'Total Revenue': 'sum',
                    'Order ID': 'count'
                })
                .round(2)
                .sort_values('Profit Margin')
                .reset_index())
    
    def custom_aggregation(self, group_by: List[str], 
                          agg_dict: Dict[str, Callable]) -> pd.DataFrame:
        """
        Perform custom aggregation.
        
        Args:
            group_by: Columns to group by
            agg_dict: Aggregation dictionary
            
        Returns:
            Aggregated DataFrame
        """
        return (self.data.groupby(group_by)
                .agg(agg_dict)
                .reset_index())
