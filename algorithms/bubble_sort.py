"""
BubbleSort implementation with visualization
"""
from typing import List
from .base_sorter import BaseSorter


class BubbleSort(BaseSorter):
    """BubbleSort algorithm"""
    
    def get_name(self) -> str:
        return "BubbleSort"
    
    def get_complexity(self) -> dict:
        return {
            'time_best': 'O(n)',
            'time_avg': 'O(n²)',
            'time_worst': 'O(n²)',
            'space': 'O(1)'
        }
    
    def sort(self, data: List[int]) -> List[int]:
        """
        Sort using BubbleSort algorithm
        
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
        
        # Bubble sort with optimization
        for i in range(n):
            swapped = False
            
            # Show current pass
            self.visualize(
                state='pass_start',
                pass_number=i,
                sorted_section=(n - i, n - 1) if i > 0 else None
            )
            
            for j in range(n - i - 1):
                # Show comparison
                self.visualize(
                    state='comparing',
                    comparing_indices=(j, j + 1),
                    sorted_section=(n - i, n - 1) if i > 0 else None
                )
                
                # Compare adjacent elements
                if not self.compare(j, j + 1):
                    # Swap if out of order
                    self.swap(j, j + 1)
                    swapped = True
                    
                    # Show swap
                    self.visualize(
                        state='swapped',
                        swap_indices=(j, j + 1),
                        sorted_section=(n - i, n - 1) if i > 0 else None
                    )
            
            # If no swaps occurred, array is sorted
            if not swapped:
                break
        
        # Final visualization
        self.visualize(state='complete')
        
        return self.data