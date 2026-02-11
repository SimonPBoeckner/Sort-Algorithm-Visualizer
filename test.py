"""
Quick test to verify installation
"""
import sys

def test_imports():
    """Test that all modules can be imported"""
    print("Testing imports...")
    
    try:
        from config import Config
        print("✓ Config imported")
        
        from data import DataGenerator, DataPattern
        print("✓ Data module imported")
        
        from visualizer import Visualizer
        print("✓ Visualizer imported")
        
        from algorithms import (
            QuickSort, MergeSort, BubbleSort,
            InsertionSort, SelectionSort
        )
        print("✓ All algorithms imported")
        
        print("\n✓ All imports successful!")
        return True
        
    except Exception as e:
        print(f"\n✗ Import failed: {e}")
        return False


def test_data_generation():
    """Test data generation"""
    print("\nTesting data generation...")
    
    try:
        from data import DataGenerator, DataPattern
        
        data = DataGenerator.generate(10, 0, 100, DataPattern.RANDOM)
        assert len(data) == 10
        print(f"✓ Random data: {data[:5]}...")
        
        data = DataGenerator.generate(10, 0, 100, DataPattern.SORTED)
        assert all(data[i] <= data[i+1] for i in range(len(data)-1))
        print(f"✓ Sorted data: {data[:5]}...")
        
        print("✓ Data generation works!")
        return True
        
    except Exception as e:
        print(f"✗ Data generation failed: {e}")
        return False


def test_sorting():
    """Test sorting without visualization"""
    print("\nTesting sorting algorithms...")
    
    try:
        from algorithms import QuickSort, MergeSort, BubbleSort
        from data import DataGenerator, DataPattern
        
        data = DataGenerator.generate(20, 0, 100, DataPattern.RANDOM)
        
        # Test QuickSort
        qs = QuickSort()
        sorted_data = qs.sort(data[:])
        assert all(sorted_data[i] <= sorted_data[i+1] for i in range(len(sorted_data)-1))
        print(f"✓ QuickSort works! Stats: {qs.get_stats()}")
        
        # Test MergeSort
        ms = MergeSort()
        sorted_data = ms.sort(data[:])
        assert all(sorted_data[i] <= sorted_data[i+1] for i in range(len(sorted_data)-1))
        print(f"✓ MergeSort works! Stats: {ms.get_stats()}")
        
        # Test BubbleSort
        bs = BubbleSort()
        sorted_data = bs.sort(data[:])
        assert all(sorted_data[i] <= sorted_data[i+1] for i in range(len(sorted_data)-1))
        print(f"✓ BubbleSort works! Stats: {bs.get_stats()}")
        
        print("✓ All sorting algorithms work!")
        return True
        
    except Exception as e:
        print(f"✗ Sorting test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    print("="*60)
    print("SORTING VISUALIZER - SYSTEM TEST")
    print("="*60)
    
    all_passed = True
    
    all_passed &= test_imports()
    all_passed &= test_data_generation()
    all_passed &= test_sorting()
    
    print("\n" + "="*60)
    if all_passed:
        print("✓ ALL TESTS PASSED!")
        print("\nYou can now run:")
        print("  python main.py quick_sort")
    else:
        print("✗ SOME TESTS FAILED")
        sys.exit(1)
    print("="*60)