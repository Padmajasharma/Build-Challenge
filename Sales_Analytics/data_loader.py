import pandas as pd
from typing import Callable, List
from functools import reduce


class DataLoader:
    """Handles CSV data loading with functional programming approach."""
    
    def __init__(self, filepath: str):
        """
        Initialize data loader.
        
        Args:
            filepath: Path to CSV file
        """
        self.filepath = filepath
        self.data = None
    
    def load_data(self) -> pd.DataFrame:
        """
        Load CSV data into DataFrame.
        
        Returns:
            Loaded DataFrame
        """
        self.data = pd.read_csv(self.filepath)
        print(f"✓ Loaded {len(self.data)} records from {self.filepath}")
        return self.data
    
    def apply_transformations(self, transformations: List[Callable]) -> pd.DataFrame:
        """
        Apply transformations using functional composition.
        
        Args:
            transformations: List of transformation functions
            
        Returns:
            Transformed DataFrame
        """
        return reduce(lambda df, func: func(df), transformations, self.data)
    
    @staticmethod
    def clean_data(df: pd.DataFrame) -> pd.DataFrame:
        """Remove null values and duplicates."""
        return df.dropna().drop_duplicates()
    
    @staticmethod
    def parse_dates(df: pd.DataFrame) -> pd.DataFrame:
        """Parse date columns."""
        date_cols = ['Order Date', 'Ship Date']
        for col in date_cols:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors='coerce')
        return df
    
    @staticmethod
    def add_calculated_fields(df: pd.DataFrame) -> pd.DataFrame:
        """Add calculated fields using lambda expressions."""
        # Profit margin percentage
        df['Profit Margin'] = df.apply(
            lambda row: (row['Total Profit'] / row['Total Revenue'] * 100) 
            if row['Total Revenue'] > 0 else 0, axis=1
        )
        
        # Processing time in days
        df['Processing Days'] = (df['Ship Date'] - df['Order Date']).dt.days
        
        # Revenue per unit
        df['Revenue Per Unit'] = df.apply(
            lambda row: row['Total Revenue'] / row['Units Sold'] 
            if row['Units Sold'] > 0 else 0, axis=1
        )
        
        # Year and Month for time series
        df['Year'] = df['Order Date'].dt.year
        df['Month'] = df['Order Date'].dt.month
        df['Year-Month'] = df['Order Date'].dt.to_period('M')
        
        return df
    
    def get_info(self) -> dict:
        """Get dataset information."""
        return {
            'total_records': len(self.data),
            'columns': list(self.data.columns),
            'regions': self.data['Region'].nunique(),
            'countries': self.data['Country'].nunique(),
            'item_types': self.data['Item Type'].nunique(),
            'date_range': f"{self.data['Order Date'].min()} to {self.data['Order Date'].max()}"
        }
