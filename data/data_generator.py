"""
Data generation utilities for sorting algorithms
"""
import numpy as np
from typing import List
from enum import Enum


class DataPattern(Enum):
    """Different types of data patterns for testing"""
    RANDOM = "random"
    SORTED = "sorted"
    REVERSED = "reversed"
    NEARLY_SORTED = "nearly_sorted"
    FEW_UNIQUE = "few_unique"
    MANY_DUPLICATES = "many_duplicates"


class DataGenerator:
    """Generate various types of data for sorting"""
    
    @staticmethod
    def generate(size: int, min_val: int, max_val: int, 
                 pattern: DataPattern = DataPattern.RANDOM) -> List[int]:
        """
        Generate data based on specified pattern
        
        Args:
            size: Number of elements
            min_val: Minimum value
            max_val: Maximum value
            pattern: Type of data pattern
            
        Returns:
            List of integers
        """
        if pattern == DataPattern.RANDOM:
            return DataGenerator._random(size, min_val, max_val)
        elif pattern == DataPattern.SORTED:
            return DataGenerator._sorted(size, min_val, max_val)
        elif pattern == DataPattern.REVERSED:
            return DataGenerator._reversed(size, min_val, max_val)
        elif pattern == DataPattern.NEARLY_SORTED:
            return DataGenerator._nearly_sorted(size, min_val, max_val)
        elif pattern == DataPattern.FEW_UNIQUE:
            return DataGenerator._few_unique(size, min_val, max_val)
        elif pattern == DataPattern.MANY_DUPLICATES:
            return DataGenerator._many_duplicates(size, min_val, max_val)
        else:
            return DataGenerator._random(size, min_val, max_val)
    
    @staticmethod
    def _random(size: int, min_val: int, max_val: int) -> List[int]:
        """Generate random data"""
        return [np.random.randint(min_val, max_val) for _ in range(size)]
    
    @staticmethod
    def _sorted(size: int, min_val: int, max_val: int) -> List[int]:
        """Generate already sorted data"""
        step = (max_val - min_val) // size
        return [min_val + i * step for i in range(size)]
    
    @staticmethod
    def _reversed(size: int, min_val: int, max_val: int) -> List[int]:
        """Generate reverse sorted data"""
        return list(reversed(DataGenerator._sorted(size, min_val, max_val)))
    
    @staticmethod
    def _nearly_sorted(size: int, min_val: int, max_val: int) -> List[int]:
        """Generate nearly sorted data with a few swaps"""
        data = DataGenerator._sorted(size, min_val, max_val)
        # Swap 10% of elements randomly
        num_swaps = max(1, size // 10)
        for _ in range(num_swaps):
            i, j = np.random.randint(0, size, 2)
            data[i], data[j] = data[j], data[i]
        return data
    
    @staticmethod
    def _few_unique(size: int, min_val: int, max_val: int) -> List[int]:
        """Generate data with only a few unique values"""
        unique_count = min(5, max_val - min_val)
        unique_values = np.random.choice(range(min_val, max_val), unique_count, replace=False)
        return [np.random.choice(unique_values) for _ in range(size)]
    
    @staticmethod
    def _many_duplicates(size: int, min_val: int, max_val: int) -> List[int]:
        """Generate data with many duplicate values"""
        unique_count = max(3, (max_val - min_val) // 10)
        unique_values = np.random.choice(range(min_val, max_val), unique_count, replace=False)
        return [np.random.choice(unique_values) for _ in range(size)]