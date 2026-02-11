"""
SelectionSort implementation with visualization
"""
from typing import List
from .base_sorter import BaseSorter


class SelectionSort(BaseSorter):
    """SelectionSort algorithm"""
    
    def get_name(self) -> str:
        return "SelectionSort"
    
    def get_complexity(self) -> dict:
        return {
            'time_best': 'O(n²)',
            'time_avg': 'O(n²)',
            'time_worst': 'O(n²)',
            'space': 'O(1)'
        }
    
    def sort(self, data: List[int]) -> List[int]:
        """
        Sort using SelectionSort algorithm
        
        Args:
            data: List to sort
            
        Returns:
            Sorted list
        """
        self.data = data[:]
        self.reset_stats()
        n = len(self.data)
        
        # Initial visualization
        self.visualize(state='initial')
        
        # Selection sort
        for i in range(n):
            # Find minimum element in unsorted portion
            min_idx = i
            
            # Show searching for minimum
            self.visualize(
                state='searching',
                current_min_idx=min_idx,
                sorted_section=(0, i - 1) if i > 0 else None,
                unsorted_section=(i, n - 1)
            )
            
            for j in range(i + 1, n):
                # Show comparison
                self.visualize(
                    state='comparing',
                    comparing_indices=(min_idx, j),
                    current_min_idx=min_idx,
                    sorted_section=(0, i - 1) if i > 0 else None
                )
                
                if not self.compare(min_idx, j):
                    min_idx = j
                    
                    # Show new minimum found
                    self.visualize(
                        state='new_min',
                        current_min_idx=min_idx,
                        sorted_section=(0, i - 1) if i > 0 else None
                    )
            
            # Swap minimum with first unsorted element
            if min_idx != i:
                self.swap(i, min_idx)
                
                # Show swap
                self.visualize(
                    state='swapped',
                    swap_indices=(i, min_idx),
                    sorted_section=(0, i)
                )
            else:
                # Show that element is already in correct position
                self.visualize(
                    state='in_place',
                    current_idx=i,
                    sorted_section=(0, i)
                )
        
        # Final visualization
        self.visualize(state='complete')
        
        return self.data