"""
Main entry point for Sorting Visualizer
"""
import sys
import argparse
from typing import Optional

from config import Config
from data import DataGenerator, DataPattern
from visualizer import Visualizer
from algorithms import get_algorithm, ALGORITHM_MAP


class SortingVisualizer:
    """Main application class"""
    
    def __init__(self, config: Optional[Config] = None):
        """
        Initialize the sorting visualizer
        
        Args:
            config: Configuration object
        """
        self.config = config or Config()
        self.visualizer = Visualizer(self.config)
        self.data = []
        
    def run(self, algorithm_name: str, data_pattern: DataPattern = DataPattern.RANDOM):
        """
        Run the sorting visualization
        
        Args:
            algorithm_name: Name of sorting algorithm
            data_pattern: Type of data pattern to generate
        """
        # Generate data
        print(f"\n{'='*60}")
        print(f"SORTING VISUALIZER")
        print(f"{'='*60}")
        print(f"Algorithm: {algorithm_name}")
        print(f"Data Size: {self.config.DATA_SIZE}")
        print(f"Data Pattern: {data_pattern.value}")
        print(f"{'='*60}\n")
        
        self.data = DataGenerator.generate(
            self.config.DATA_SIZE,
            self.config.DATA_MIN,
            self.config.DATA_MAX,
            data_pattern
        )
        
        # Get algorithm
        AlgorithmClass = get_algorithm(algorithm_name)
        if not AlgorithmClass:
            print(f"Error: Algorithm '{algorithm_name}' not found!")
            print(f"Available algorithms: {', '.join(ALGORITHM_MAP.keys())}")
            return
        
        # Setup visualizer callback
        def visualize_callback(**kwargs):
            stats = kwargs.pop('stats', None)
            if self.config.SHOW_STATS and hasattr(algorithm, 'get_stats'):
                stats = algorithm.get_stats()
            self.visualizer.visualize(stats=stats, **kwargs)
        
        # Create algorithm instance with visualizer
        algorithm = AlgorithmClass(visualizer=visualize_callback)
        
        # Setup visualization
        self.visualizer.setup(self.data, algorithm.get_name())
        
        # Print algorithm info
        complexity = algorithm.get_complexity()
        print(f"Time Complexity:")
        print(f"  Best Case:  {complexity['time_best']}")
        print(f"  Average:    {complexity['time_avg']}")
        print(f"  Worst Case: {complexity['time_worst']}")
        print(f"Space Complexity: {complexity['space']}")
        print(f"\nStarting visualization...\n")
        
        # Sort
        sorted_data = algorithm.sort(self.data)
        
        # Print statistics
        stats = algorithm.get_stats()
        print(f"\n{'='*60}")
        print(f"SORTING COMPLETE")
        print(f"{'='*60}")
        print(f"Comparisons: {stats['comparisons']}")
        print(f"Swaps:       {stats['swaps']}")
        print(f"Accesses:    {stats['accesses']}")
        print(f"{'='*60}\n")
        
        # Verify sort
        is_sorted = all(sorted_data[i] <= sorted_data[i+1] for i in range(len(sorted_data)-1))
        print(f"Verification: {'✓ PASSED' if is_sorted else '✗ FAILED'}")
        
        # Finalize visualization
        self.visualizer.finalize()


def main():
    """Main function with CLI argument parsing"""
    parser = argparse.ArgumentParser(
        description='Sorting Algorithm Visualizer',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py quick_sort
  python main.py merge_sort --size 50 --delay 0.1
  python main.py bubble_sort --pattern nearly_sorted
  python main.py insertion_sort --size 30 --delay 0.05 --pattern reversed
        """
    )
    
    parser.add_argument(
        'algorithm',
        choices=list(ALGORITHM_MAP.keys()),
        help='Sorting algorithm to visualize'
    )
    
    parser.add_argument(
        '--size',
        type=int,
        default=Config.DATA_SIZE,
        help=f'Number of elements to sort (default: {Config.DATA_SIZE})'
    )
    
    parser.add_argument(
        '--min',
        type=int,
        default=Config.DATA_MIN,
        help=f'Minimum value (default: {Config.DATA_MIN})'
    )
    
    parser.add_argument(
        '--max',
        type=int,
        default=Config.DATA_MAX,
        help=f'Maximum value (default: {Config.DATA_MAX})'
    )
    
    parser.add_argument(
        '--delay',
        type=float,
        default=Config.ANIMATION_DELAY,
        help=f'Animation delay in seconds (default: {Config.ANIMATION_DELAY})'
    )
    
    parser.add_argument(
        '--pattern',
        choices=[p.value for p in DataPattern],
        default=DataPattern.RANDOM.value,
        help='Data pattern to generate (default: random)'
    )
    
    parser.add_argument(
        '--no-stats',
        action='store_true',
        help='Hide statistics display'
    )
    
    args = parser.parse_args()
    
    # Update config
    Config.update(
        data_size=args.size,
        data_min=args.min,
        data_max=args.max,
        animation_delay=args.delay,
        show_stats=not args.no_stats
    )
    
    # Create and run visualizer
    visualizer = SortingVisualizer()
    data_pattern = DataPattern(args.pattern)
    visualizer.run(args.algorithm, data_pattern)


if __name__ == '__main__':
    main()