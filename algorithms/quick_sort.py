"""
QuickSort implementation with visualization
"""
from typing import List
from random import randrange
from .base_sorter import BaseSorter


class QuickSort(BaseSorter):
    """QuickSort algorithm with in-place sorting"""
    
    def get_name(self) -> str:
        return "QuickSort"
    
    def get_complexity(self) -> dict:
        return {
            'time_best': 'O(n log n)',
            'time_avg': 'O(n log n)',
            'time_worst': 'O(n²)',
            'space': 'O(log n)'
        }
    
    def sort(self, data: List[int]) -> List[int]:
        """
        Sort using QuickSort algorithm
        
        Args:
            data: List to sort
            
        Returns:
            Sorted list
        """
        self.data = data[:]
        self.reset_stats()
        
        # Initial visualization
        self.visualize(state='initial')
        
        # Sort
        self._quicksort(0, len(self.data) - 1)
        
        # Final visualization
        self.visualize(state='complete')
        
        return self.data
    
    def _quicksort(self, low: int, high: int):
        """
        Recursive quicksort implementation
        
        Args:
            low: Starting index
            high: Ending index
        """
        if low >= high:
            return
        
        # Show the section being worked on
        self.visualize(
            state='working',
            section_range=(low, high)
        )
        
        # Partition and get pivot position
        pivot_idx = self._partition(low, high)
        
        # Recursively sort left and right partitions
        self._quicksort(low, pivot_idx - 1)
        self._quicksort(pivot_idx + 1, high)
    
    def _partition(self, low: int, high: int) -> int:
        """
        Partition the array around a pivot
        
        Args:
            low: Starting index
            high: Ending index
            
        Returns:
            Final position of pivot
        """
        # Choose random pivot and move to end
        pivot_idx = randrange(low, high + 1)
        pivot_value = self.data[pivot_idx]
        
        # Show pivot selection
        self.visualize(
            state='pivot_selected',
            pivot_idx=pivot_idx,
            section_range=(low, high)
        )
        
        # Move pivot to end
        self.swap(pivot_idx, high)
        pivot_idx = high
        
        # Partition
        i = low
        left_indices = []
        right_indices = []
        
        for j in range(low, high):
            if self.compare(j, pivot_idx):
                left_indices.append(j)
            else:
                right_indices.append(j)
        
        # Show partitioning
        self.visualize(
            state='partitioning',
            pivot_idx=pivot_idx,
            left_indices=left_indices,
            right_indices=right_indices,
            section_range=(low, high)
        )
        
        # Move elements smaller than pivot to the left
        i = low
        for j in range(low, high):
            if self.compare(j, pivot_idx):
                if i != j:
                    self.swap(i, j)
                    self.visualize(
                        state='swapping',
                        swap_indices=(i, j),
                        pivot_idx=pivot_idx,
                        section_range=(low, high)
                    )
                i += 1
        
        # Place pivot in final position
        self.swap(i, high)
        
        # Show pivot in final position
        self.visualize(
            state='pivot_placed',
            pivot_idx=i,
            section_range=(low, high)
        )
        
        return i