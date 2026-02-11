"""
Sorting algorithms package
"""
from .base_sorter import BaseSorter
from .quick_sort import QuickSort
from .merge_sort import MergeSort
from .bubble_sort import BubbleSort
from .insertion_sort import InsertionSort
from .selection_sort import SelectionSort

__all__ = [
    'BaseSorter',
    'QuickSort',
    'MergeSort',
    'BubbleSort',
    'InsertionSort',
    'SelectionSort'
]

# Algorithm registry for easy access
ALGORITHM_MAP = {
    'quick_sort': QuickSort,
    'merge_sort': MergeSort,
    'bubble_sort': BubbleSort,
    'insertion_sort': InsertionSort,
    'selection_sort': SelectionSort
}


def get_algorithm(name: str):
    """
    Get algorithm class by name
    
    Args:
        name: Algorithm name
        
    Returns:
        Algorithm class
    """
    return ALGORITHM_MAP.get(name.lower())