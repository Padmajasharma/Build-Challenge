import pandas as pd
from typing import Callable, Any, List
from functools import reduce
import operator


class StreamOperations:
    """Implements stream-like operations on DataFrame."""
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize with data.
        
        Args:
            data: Input DataFrame
        """
        self.data = data.copy()
    
    def filter(self, predicate: Callable) -> 'StreamOperations':
        """
        Filter records using predicate (similar to Stream.filter).
        
        Args:
            predicate: Boolean function
            
        Returns:
            StreamOperations with filtered data
        """
        filtered = self.data[self.data.apply(predicate, axis=1)]
        return StreamOperations(filtered)
    
    def map(self, mapper: Callable) -> pd.Series:
        """
        Transform each record (similar to Stream.map).
        
        Args:
            mapper: Transformation function
            
        Returns:
            Series of transformed values
        """
        return self.data.apply(mapper, axis=1)
    
    def sorted_by(self, key: str, ascending: bool = True) -> 'StreamOperations':
        """
        Sort data by key (similar to Stream.sorted).
        
        Args:
            key: Column name
            ascending: Sort order
            
        Returns:
            StreamOperations with sorted data
        """
        sorted_data = self.data.sort_values(by=key, ascending=ascending)
        return StreamOperations(sorted_data)
    
    def limit(self, n: int) -> 'StreamOperations':
        """
        Limit to n records (similar to Stream.limit).
        
        Args:
            n: Number of records
            
        Returns:
            StreamOperations with limited data
        """
        return StreamOperations(self.data.head(n))
    
    def skip(self, n: int) -> 'StreamOperations':
        """
        Skip first n records (similar to Stream.skip).
        
        Args:
            n: Number to skip
            
        Returns:
            StreamOperations with remaining data
        """
        return StreamOperations(self.data.iloc[n:])
    
    def distinct(self, column: str = None) -> List[Any]:
        """
        Get distinct values (similar to Stream.distinct).
        
        Args:
            column: Column name (if None, returns unique rows)
            
        Returns:
            List of distinct values
        """
        if column:
            return self.data[column].unique().tolist()
        return self.data.drop_duplicates().values.tolist()
    
    def collect(self) -> pd.DataFrame:
        """
        Collect results (terminal operation).
        
        Returns:
            DataFrame
        """
        return self.data
    
    def count(self) -> int:
        """
        Count records (terminal operation).
        
        Returns:
            Number of records
        """
        return len(self.data)
    
    def reduce_sum(self, column: str) -> float:
        """
        Sum values in column (similar to Stream.reduce).
        
        Args:
            column: Column name
            
        Returns:
            Sum of values
        """
        return reduce(operator.add, self.data[column], 0)
    
    def reduce_custom(self, column: str, operation: Callable, initial: Any = 0) -> Any:
        """
        Custom reduce operation.
        
        Args:
            column: Column name
            operation: Reduction function
            initial: Initial value
            
        Returns:
            Reduced value
        """
        return reduce(operation, self.data[column], initial)
    
    def any_match(self, predicate: Callable) -> bool:
        """
        Check if any record matches (similar to Stream.anyMatch).
        
        Args:
            predicate: Predicate function
            
        Returns:
            True if any match
        """
        return self.data.apply(predicate, axis=1).any()
    
    def all_match(self, predicate: Callable) -> bool:
        """
        Check if all records match (similar to Stream.allMatch).
        
        Args:
            predicate: Predicate function
            
        Returns:
            True if all match
        """
        return self.data.apply(predicate, axis=1).all()
    
    def none_match(self, predicate: Callable) -> bool:
        """
        Check if no records match (similar to Stream.noneMatch).
        
        Args:
            predicate: Predicate function
            
        Returns:
            True if none match
        """
        return not self.any_match(predicate)
    
    def find_first(self) -> pd.Series:
        """
        Get first record (similar to Stream.findFirst).
        
        Returns:
            First record
        """
        return self.data.iloc[0] if len(self.data) > 0 else None
    
    def find_any(self) -> pd.Series:
        """
        Get any record (similar to Stream.findAny).
        
        Returns:
            Random record
        """
        return self.data.sample(1).iloc[0] if len(self.data) > 0 else None