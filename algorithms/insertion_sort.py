"""
InsertionSort implementation with visualization
"""
from typing import List
from .base_sorter import BaseSorter


class InsertionSort(BaseSorter):
    """InsertionSort algorithm"""
    
    def get_name(self) -> str:
        return "InsertionSort"
    
    def get_complexity(self) -> dict:
        return {
            'time_best': 'O(n)',
            'time_avg': 'O(n²)',
            'time_worst': 'O(n²)',
            'space': 'O(1)'
        }
    
    def sort(self, data: List[int]) -> List[int]:
        """
        Sort using InsertionSort algorithm
        
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
        
        # Insertion sort
        for i in range(1, n):
            key = self.data[i]
            self.accesses += 1
            
            # Show current element being inserted
            self.visualize(
                state='selecting',
                current_idx=i,
                sorted_section=(0, i - 1)
            )
            
            j = i - 1
            
            # Move elements greater than key one position ahead
            while j >= 0:
                self.comparisons += 1
                self.accesses += 1
                
                # Show comparison
                self.visualize(
                    state='comparing',
                    comparing_indices=(j, i),
                    sorted_section=(0, i - 1)
                )
                
                if self.data[j] > key:
                    self.data[j + 1] = self.data[j]
                    self.accesses += 1
                    
                    # Show shift
                    self.visualize(
                        state='shifting',
                        shift_from=j,
                        shift_to=j + 1,
                        sorted_section=(0, i - 1)
                    )
                    j -= 1
                else:
                    break
            
            # Insert key in correct position
            self.data[j + 1] = key
            self.accesses += 1
            
            # Show insertion
            self.visualize(
                state='inserted',
                inserted_idx=j + 1,
                sorted_section=(0, i)
            )
        
        # Final visualization
        self.visualize(state='complete')
        
        return self.data