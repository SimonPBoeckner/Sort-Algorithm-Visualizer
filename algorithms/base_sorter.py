"""
Abstract base class for sorting algorithms
"""
from abc import ABC, abstractmethod
from typing import List, Callable, Optional


class BaseSorter(ABC):
    """Abstract base class for all sorting algorithms"""
    
    def __init__(self, visualizer=None):
        """
        Initialize sorter
        
        Args:
            visualizer: Callback function for visualization (optional)
        """
        self.visualizer = visualizer
        self.data: List[int] = []
        self.comparisons = 0
        self.swaps = 0
        self.accesses = 0
        
    def reset_stats(self):
        """Reset statistics counters"""
        self.comparisons = 0
        self.swaps = 0
        self.accesses = 0
    
    def compare(self, i: int, j: int) -> bool:
        """
        Compare two elements and track statistics
        
        Args:
            i: First index
            j: Second index
            
        Returns:
            True if data[i] <= data[j]
        """
        self.comparisons += 1
        self.accesses += 2
        return self.data[i] <= self.data[j]
    
    def swap(self, i: int, j: int):
        """
        Swap two elements and track statistics
        
        Args:
            i: First index
            j: Second index
        """
        self.swaps += 1
        self.accesses += 4  # 2 reads, 2 writes
        self.data[i], self.data[j] = self.data[j], self.data[i]
    
    def visualize(self, **kwargs):
        """
        Call the visualizer with current state
        
        Args:
            **kwargs: Visualization parameters
        """
        if self.visualizer:
            self.visualizer(data=self.data, **kwargs)
    
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        """
        Sort the data
        
        Args:
            data: List to sort
            
        Returns:
            Sorted list
        """
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        """Return the name of the sorting algorithm"""
        pass
    
    @abstractmethod
    def get_complexity(self) -> dict:
        """
        Return time and space complexity
        
        Returns:
            Dictionary with 'time_best', 'time_avg', 'time_worst', 'space'
        """
        pass
    
    def get_stats(self) -> dict:
        """
        Get statistics from the last sort
        
        Returns:
            Dictionary with comparisons, swaps, and accesses
        """
        return {
            'comparisons': self.comparisons,
            'swaps': self.swaps,
            'accesses': self.accesses
        }