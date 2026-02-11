"""
Configuration file for Sorting Visualizer
All tuneable parameters in one place
"""

class Config:
    # Data Generation
    DATA_SIZE = 100
    DATA_MIN = 0
    DATA_MAX = 100
    
    # Visualization Settings
    FIG_WIDTH = 14
    FIG_HEIGHT = 7
    ANIMATION_DELAY = 0.05  # seconds between frames
    
    # Color Scheme
    COLORS = {
        'default': 'lightblue',
        'active_section': 'blue',
        'pivot': 'red',
        'left_partition': 'green',
        'right_partition': 'orange',
        'comparing': 'yellow',
        'sorted': 'purple',
        'swapping': 'magenta'
    }
    
    # Algorithm Settings
    AVAILABLE_ALGORITHMS = [
        'quick_sort',
        'merge_sort',
        'bubble_sort',
        'insertion_sort',
        'selection_sort'
    ]
    
    DEFAULT_ALGORITHM = 'quick_sort'
    
    # Display Options
    SHOW_TITLE = True
    SHOW_LEGEND = True
    SHOW_STATS = True  # Show comparison/swap counts
    
    @classmethod
    def update(cls, **kwargs):
        """Update configuration values"""
        for key, value in kwargs.items():
            if hasattr(cls, key.upper()):
                setattr(cls, key.upper(), value)