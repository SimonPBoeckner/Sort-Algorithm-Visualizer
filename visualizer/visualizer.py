"""
Visualization engine for sorting algorithms
"""
import matplotlib.pyplot as plt
from typing import List, Optional, Tuple
from config import Config


class Visualizer:
    """Handles visualization of sorting algorithms"""
    
    def __init__(self, config=None):
        """
        Initialize visualizer
        
        Args:
            config: Configuration object (optional)
        """
        self.config = config if config is not None else Config()
        self.fig, self.ax = plt.subplots(
            figsize=(self.config.FIG_WIDTH, self.config.FIG_HEIGHT)
        )
        self.data = []
        self.algorithm_name = ""
        
    def setup(self, data: List[int], algorithm_name: str):
        """
        Setup visualization for a new sort
        
        Args:
            data: Initial data
            algorithm_name: Name of algorithm
        """
        self.data = data
        self.algorithm_name = algorithm_name
        plt.ion()  # Turn on interactive mode
        
    def visualize(self, data: List[int], state: str = 'working', **kwargs):
        """
        Visualize current state of sorting
        
        Args:
            data: Current data state
            state: Current state of algorithm
            **kwargs: Additional visualization parameters
        """
        self.data = data
        self.ax.clear()
        
        # Get colors for bars
        colors = self._get_colors(state, **kwargs)
        
        # Draw bars
        bars = self.ax.bar(range(len(data)), data, color=colors, edgecolor='black', linewidth=0.5)
        
        # Set title
        title = self._get_title(state, **kwargs)
        self.ax.set_title(title, fontsize=14, fontweight='bold')
        
        # Set labels
        self.ax.set_xlabel("Index", fontsize=10)
        self.ax.set_ylabel("Value", fontsize=10)
        
        # Set limits
        self.ax.set_xlim(-1, len(data))
        self.ax.set_ylim(0, max(data) * 1.1 if data else 100)
        
        # Add legend if enabled
        if self.config.SHOW_LEGEND and state != 'initial' and state != 'complete':
            self._add_legend(state, **kwargs)
        
        # Add stats if enabled
        if self.config.SHOW_STATS and 'stats' in kwargs:
            self._add_stats(kwargs['stats'])
        
        plt.pause(self.config.ANIMATION_DELAY)
    
    def _get_colors(self, state: str, **kwargs) -> List[str]:
        """
        Determine bar colors based on state
        
        Args:
            state: Current state
            **kwargs: Additional parameters
            
        Returns:
            List of colors
        """
        colors = [self.config.COLORS['default']] * len(self.data)
        
        if state == 'complete':
            colors = [self.config.COLORS['sorted']] * len(self.data)
            return colors
        
        # Highlight sorted section
        if 'sorted_section' in kwargs and kwargs['sorted_section'] is not None:
            start, end = kwargs['sorted_section']
            for i in range(start, min(end + 1, len(colors))):
                colors[i] = self.config.COLORS['sorted']
        
        # Highlight active section
        if 'section_range' in kwargs:
            start, end = kwargs['section_range']
            for i in range(start, min(end + 1, len(colors))):
                if colors[i] == self.config.COLORS['default']:
                    colors[i] = self.config.COLORS['active_section']
        
        # Highlight pivot
        if 'pivot_idx' in kwargs and kwargs['pivot_idx'] is not None:
            idx = kwargs['pivot_idx']
            if 0 <= idx < len(colors):
                colors[idx] = self.config.COLORS['pivot']
        
        # Highlight left partition
        if 'left_indices' in kwargs and kwargs['left_indices'] is not None:
            for idx in kwargs['left_indices']:
                if 0 <= idx < len(colors):
                    colors[idx] = self.config.COLORS['left_partition']
        
        # Highlight right partition
        if 'right_indices' in kwargs and kwargs['right_indices'] is not None:
            for idx in kwargs['right_indices']:
                if 0 <= idx < len(colors):
                    colors[idx] = self.config.COLORS['right_partition']
        
        # Highlight comparing elements
        if 'comparing_indices' in kwargs:
            for idx in kwargs['comparing_indices']:
                if 0 <= idx < len(colors):
                    colors[idx] = self.config.COLORS['comparing']
        
        # Highlight swapping elements
        if 'swap_indices' in kwargs:
            for idx in kwargs['swap_indices']:
                if 0 <= idx < len(colors):
                    colors[idx] = self.config.COLORS['swapping']
        
        # Highlight current element
        if 'current_idx' in kwargs and kwargs['current_idx'] is not None:
            idx = kwargs['current_idx']
            if 0 <= idx < len(colors) and colors[idx] == self.config.COLORS['default']:
                colors[idx] = self.config.COLORS['comparing']
        
        return colors
    
    def _get_title(self, state: str, **kwargs) -> str:
        """
        Generate title based on state
        
        Args:
            state: Current state
            **kwargs: Additional parameters
            
        Returns:
            Title string
        """
        base = f"{self.algorithm_name}"
        
        if state == 'initial':
            return f"{base} - Initial State"
        elif state == 'complete':
            return f"{base} - Sorting Complete!"
        elif state == 'pivot_selected':
            return f"{base} - Pivot Selected"
        elif state == 'partitioning':
            return f"{base} - Partitioning Around Pivot"
        elif state == 'comparing':
            return f"{base} - Comparing Elements"
        elif state == 'swapped':
            return f"{base} - Elements Swapped"
        elif state == 'merging':
            return f"{base} - Merging Subarrays"
        elif state == 'searching':
            return f"{base} - Searching for Minimum"
        else:
            return f"{base} - Sorting in Progress"
    
    def _add_legend(self, state: str, **kwargs):
        """Add legend to plot"""
        from matplotlib.patches import Patch
        
        legend_elements = []
        
        # Add relevant legend items based on current state
        if 'pivot_idx' in kwargs:
            legend_elements.append(
                Patch(facecolor=self.config.COLORS['pivot'], label='Pivot')
            )
        
        if 'left_indices' in kwargs or 'left_partition' in kwargs:
            legend_elements.append(
                Patch(facecolor=self.config.COLORS['left_partition'], label='≤ Pivot')
            )
        
        if 'right_indices' in kwargs or 'right_partition' in kwargs:
            legend_elements.append(
                Patch(facecolor=self.config.COLORS['right_partition'], label='> Pivot')
            )
        
        if 'comparing_indices' in kwargs:
            legend_elements.append(
                Patch(facecolor=self.config.COLORS['comparing'], label='Comparing')
            )
        
        if 'sorted_section' in kwargs and kwargs['sorted_section'] is not None:
            legend_elements.append(
                Patch(facecolor=self.config.COLORS['sorted'], label='Sorted')
            )
        
        if legend_elements:
            self.ax.legend(handles=legend_elements, loc='upper right', fontsize=8)
    
    def _add_stats(self, stats: dict):
        """
        Add statistics text to plot
        
        Args:
            stats: Statistics dictionary
        """
        stats_text = (
            f"Comparisons: {stats.get('comparisons', 0)}\n"
            f"Swaps: {stats.get('swaps', 0)}\n"
            f"Accesses: {stats.get('accesses', 0)}"
        )
        self.ax.text(
            0.02, 0.98, stats_text,
            transform=self.ax.transAxes,
            fontsize=9,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        )
    
    def finalize(self):
        """Finalize visualization"""
        plt.ioff()
        plt.show()