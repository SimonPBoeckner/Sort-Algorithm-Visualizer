"""
MergeSort implementation with visualization
"""
from typing import List
from .base_sorter import BaseSorter


class MergeSort(BaseSorter):
    """MergeSort algorithm"""
    
    def get_name(self) -> str:
        return "MergeSort"
    
    def get_complexity(self) -> dict:
        return {
            'time_best': 'O(n log n)',
            'time_avg': 'O(n log n)',
            'time_worst': 'O(n log n)',
            'space': 'O(n)'
        }
    
    def sort(self, data: List[int]) -> List[int]:
        """
        Sort using MergeSort algorithm
        
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
        self._mergesort(0, len(self.data) - 1)
        
        # Final visualization
        self.visualize(state='complete')
        
        return self.data
    
    def _mergesort(self, left: int, right: int):
        """
        Recursive mergesort implementation
        
        Args:
            left: Starting index
            right: Ending index
        """
        if left >= right:
            return
        
        mid = (left + right) // 2
        
        # Show the section being divided
        self.visualize(
            state='dividing',
            section_range=(left, right),
            mid_point=mid
        )
        
        # Recursively sort left and right halves
        self._mergesort(left, mid)
        self._mergesort(mid + 1, right)
        
        # Merge the sorted halves
        self._merge(left, mid, right)
    
    def _merge(self, left: int, mid: int, right: int):
        """
        Merge two sorted subarrays
        
        Args:
            left: Starting index
            mid: Middle index
            right: Ending index
        """
        # Create copies of the subarrays
        left_copy = self.data[left:mid + 1]
        right_copy = self.data[mid + 1:right + 1]
        
        # Show merging sections
        self.visualize(
            state='merging',
            left_section=(left, mid),
            right_section=(mid + 1, right)
        )
        
        # Merge
        i = j = 0
        k = left
        
        while i < len(left_copy) and j < len(right_copy):
            self.comparisons += 1
            self.accesses += 2
            
            if left_copy[i] <= right_copy[j]:
                self.data[k] = left_copy[i]
                self.accesses += 1
                i += 1
            else:
                self.data[k] = right_copy[j]
                self.accesses += 1
                j += 1
            
            # Show merge progress
            self.visualize(
                state='merge_progress',
                section_range=(left, right),
                current_idx=k
            )
            k += 1
        
        # Copy remaining elements
        while i < len(left_copy):
            self.data[k] = left_copy[i]
            self.accesses += 1
            i += 1
            k += 1
        
        while j < len(right_copy):
            self.data[k] = right_copy[j]
            self.accesses += 1
            j += 1
            k += 1
        
        # Show merged section
        self.visualize(
            state='merged',
            section_range=(left, right)
        )