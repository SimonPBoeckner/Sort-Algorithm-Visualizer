"""
Example usage of Sorting Visualizer as a library
"""
from config import Config
from data import DataGenerator, DataPattern
from visualizer import Visualizer
from algorithms import QuickSort, MergeSort, BubbleSort


def example_basic():
    """Basic usage example"""
    print("Example 1: Basic QuickSort visualization\n")
    
    # Generate data
    data = DataGenerator.generate(50, 0, 100, DataPattern.RANDOM)
    
    # Create visualizer
    visualizer = Visualizer()
    
    # Create algorithm with visualizer callback
    def vis_callback(**kwargs):
        visualizer.visualize(**kwargs)
    
    algorithm = QuickSort(visualizer=vis_callback)
    
    # Setup and run
    visualizer.setup(data, algorithm.get_name())
    sorted_data = algorithm.sort(data)
    
    # Print stats
    stats = algorithm.get_stats()
    print(f"Comparisons: {stats['comparisons']}")
    print(f"Swaps: {stats['swaps']}")
    
    visualizer.finalize()


def example_custom_config():
    """Example with custom configuration"""
    print("Example 2: MergeSort with custom settings\n")
    
    # Customize configuration
    Config.update(
        data_size=80,
        animation_delay=0.1,
        show_stats=True
    )
    
    # Generate nearly-sorted data
    data = DataGenerator.generate(
        Config.DATA_SIZE,
        Config.DATA_MIN,
        Config.DATA_MAX,
        DataPattern.NEARLY_SORTED
    )
    
    # Create and run
    visualizer = Visualizer()
    
    def vis_callback(**kwargs):
        stats = algorithm.get_stats()
        visualizer.visualize(stats=stats, **kwargs)
    
    algorithm = MergeSort(visualizer=vis_callback)
    
    visualizer.setup(data, algorithm.get_name())
    sorted_data = algorithm.sort(data)
    visualizer.finalize()


def example_compare_algorithms():
    """Compare multiple algorithms (no visualization)"""
    print("Example 3: Comparing algorithm performance\n")
    
    # Generate test data
    data = DataGenerator.generate(100, 0, 100, DataPattern.RANDOM)
    
    algorithms = [
        QuickSort(),
        MergeSort(),
        BubbleSort()
    ]
    
    print(f"{'Algorithm':<15} {'Comparisons':<12} {'Swaps':<8} {'Accesses':<10}")
    print("-" * 50)
    
    for algo in algorithms:
        algo.sort(data[:])  # Sort copy of data
        stats = algo.get_stats()
        print(f"{algo.get_name():<15} {stats['comparisons']:<12} "
              f"{stats['swaps']:<8} {stats['accesses']:<10}")


if __name__ == '__main__':
    # Run examples
    # Uncomment the one you want to try
    
    example_basic()
    # example_custom_config()
    # example_compare_algorithms()