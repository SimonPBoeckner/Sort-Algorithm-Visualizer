# Sorting Algorithm Visualizer 🎨

A comprehensive, extensible sorting algorithm visualizer built with Python and Matplotlib. Watch different sorting algorithms work in real-time with beautiful visualizations!

## Features ✨

- **Multiple Sorting Algorithms**: QuickSort, MergeSort, BubbleSort, InsertionSort, SelectionSort
- **Real-time Visualization**: See every comparison, swap, and partition
- **Statistics Tracking**: Monitor comparisons, swaps, and array accesses
- **Flexible Data Patterns**: Test with random, sorted, reversed, or nearly-sorted data
- **Customizable Parameters**: Adjust size, speed, colors, and more
- **Extensible Architecture**: Easy to add new algorithms
- **Clean Code Structure**: Modular design with separation of concerns

## Project Structure 📁

```
sorting_visualizer/
├── main.py                 # Entry point with CLI
├── config.py              # Configuration settings
├── data/
│   ├── __init__.py
│   └── data_generator.py  # Data generation utilities
├── visualizer/
│   ├── __init__.py
│   └── visualizer.py      # Visualization engine
├── algorithms/
│   ├── __init__.py
│   ├── base_sorter.py     # Abstract base class
│   ├── quick_sort.py      # QuickSort implementation
│   ├── merge_sort.py      # MergeSort implementation
│   ├── bubble_sort.py     # BubbleSort implementation
│   ├── insertion_sort.py  # InsertionSort implementation
│   └── selection_sort.py  # SelectionSort implementation
└── utils/
    └── __init__.py
```

## Installation 🚀

1. Clone or download this project
2. Install required dependencies:

```bash
pip install matplotlib numpy
```

## Usage 💻

### Basic Usage

Run a sorting algorithm with default settings:

```bash
python main.py quick_sort
```

### Custom Parameters

Adjust size, speed, and data pattern:

```bash
# Sort 50 elements with slower animation
python main.py merge_sort --size 50 --delay 0.1

# Sort nearly-sorted data
python main.py bubble_sort --pattern nearly_sorted

# Sort reversed data with custom range
python main.py insertion_sort --size 30 --min 10 --max 200 --pattern reversed
```

### Command Line Options

```
positional arguments:
  algorithm           Sorting algorithm to visualize
                      Choices: quick_sort, merge_sort, bubble_sort, 
                               insertion_sort, selection_sort

optional arguments:
  --size SIZE         Number of elements to sort (default: 100)
  --min MIN          Minimum value (default: 0)
  --max MAX          Maximum value (default: 100)
  --delay DELAY      Animation delay in seconds (default: 0.05)
  --pattern PATTERN  Data pattern to generate
                     Choices: random, sorted, reversed, nearly_sorted,
                              few_unique, many_duplicates
  --no-stats         Hide statistics display
```

## Available Algorithms 🧮

| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| QuickSort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| MergeSort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| BubbleSort | O(n) | O(n²) | O(n²) | O(1) |
| InsertionSort | O(n) | O(n²) | O(n²) | O(1) |
| SelectionSort | O(n²) | O(n²) | O(n²) | O(1) |

## Customization 🎨

### Modify Configuration

Edit `config.py` to change default settings:

```python
class Config:
    DATA_SIZE = 100          # Number of elements
    ANIMATION_DELAY = 0.05   # Speed of animation
    
    COLORS = {
        'pivot': 'red',
        'sorted': 'purple',
        # ... customize colors
    }
```

### Add New Algorithms

1. Create a new file in `algorithms/` (e.g., `heap_sort.py`)
2. Inherit from `BaseSorter`:

```python
from .base_sorter import BaseSorter

class HeapSort(BaseSorter):
    def get_name(self) -> str:
        return "HeapSort"
    
    def get_complexity(self) -> dict:
        return {
            'time_best': 'O(n log n)',
            'time_avg': 'O(n log n)',
            'time_worst': 'O(n log n)',
            'space': 'O(1)'
        }
    
    def sort(self, data: List[int]) -> List[int]:
        self.data = data[:]
        self.reset_stats()
        
        # Your implementation here
        # Use self.visualize() to show steps
        # Use self.compare() and self.swap() for tracking
        
        return self.data
```

3. Add to `algorithms/__init__.py`:

```python
from .heap_sort import HeapSort

ALGORITHM_MAP = {
    # ... existing algorithms
    'heap_sort': HeapSort
}
```

## Color Coding 🌈

- **Light Blue**: Unsorted elements
- **Blue**: Current working section
- **Red**: Pivot element
- **Green**: Elements ≤ pivot
- **Orange**: Elements > pivot
- **Yellow**: Elements being compared
- **Magenta**: Elements being swapped
- **Purple**: Sorted elements

## Examples 📸

### QuickSort
```bash
python main.py quick_sort --size 80 --delay 0.08
```

### MergeSort
```bash
python main.py merge_sort --size 60 --pattern nearly_sorted
```

### BubbleSort (slower algorithm, smaller size recommended)
```bash
python main.py bubble_sort --size 30 --delay 0.1
```

## Tips 💡

- Use **smaller sizes (30-50)** for slower algorithms (Bubble, Insertion, Selection)
- Use **larger sizes (100-200)** for faster algorithms (Quick, Merge)
- Adjust **--delay** to speed up or slow down animations
- Try different **patterns** to see how algorithms perform on different data
- Use **--no-stats** for cleaner visualization without statistics

## Contributing 🤝

Feel free to:
- Add new sorting algorithms
- Improve visualizations
- Add new data patterns
- Enhance documentation
- Report bugs or suggest features

## License 📄

Free to use and modify!

## Credits 👨‍💻

Built with ❤️ using Python, Matplotlib, and NumPy