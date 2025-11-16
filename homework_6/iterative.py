import time
import random
from typing import List, Callable, Any
import sys
sys.setrecursionlimit(1000000)

def timing_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"{func.__name__}: {execution_time:.6f} сек")
        return result
    return wrapper

def iterative_mergesort(arr: List) -> List:
    n = len(arr)
    if n <= 1:
        return arr.copy()
    
    arr = arr.copy()
    width = 1
    
    while width < n:
        for i in range(0, n, 2 * width):
            left = i
            mid = min(i + width, n)
            right = min(i + 2 * width, n)
            
            merged = []
            l, r = left, mid
            
            while l < mid and r < right:
                if arr[l] <= arr[r]:
                    merged.append(arr[l])
                    l += 1
                else:
                    merged.append(arr[r])
                    r += 1
            
            merged.extend(arr[l:mid])
            merged.extend(arr[r:right])
            arr[left:right] = merged
        
        width *= 2
    
    return arr

def iterative_quicksort(arr: List) -> List:
    if len(arr) <= 1:
        return arr.copy()
    
    arr = arr.copy()
    stack = [(0, len(arr) - 1)]
    
    while stack:
        left, right = stack.pop()
        
        if left >= right:
            continue
        
        pivot = arr[left]
        i = left + 1
        
        for j in range(left + 1, right + 1):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        
        arr[left], arr[i - 1] = arr[i - 1], arr[left]
        pivot_index = i - 1
        
        if pivot_index - left > right - pivot_index:
            stack.append((left, pivot_index - 1))
            stack.append((pivot_index + 1, right))
        else:
            stack.append((pivot_index + 1, right))
            stack.append((left, pivot_index - 1))
    
    return arr

def generate_many_duplicates(n: int) -> List[int]:
    return [random.randint(0, 10) for _ in range(n)]

def generate_geometric_progression(n: int) -> List[int]:
    return [int(1.1 ** i) for i in range(int(n))]

def generate_sorted_blocks(n: int) -> List[int]:
    block_size = max(10, n // 100) 
    arr = []
    current = 0
    
    while len(arr) < n:
        block_length = random.randint(block_size // 2, block_size * 2)
        block = list(range(current, current + block_length))
        if random.random() > 0.5:
            block.reverse() 
        arr.extend(block)
        current += block_length
    
    return arr[:n]

def generate_test_cases(size: int = 10000) -> dict:
    return {
        'много_дубликатов': generate_many_duplicates(size),
        'геометрическая_прогрессия': generate_geometric_progression(size // 10),
        'блоки_отсортированных': generate_sorted_blocks(size),
    }

@timing_decorator
def test_iterative_mergesort(arr: List) -> List:
    return iterative_mergesort(arr)

@timing_decorator
def test_iterative_quicksort(arr: List) -> List:
    return iterative_quicksort(arr)

def run_tests():
    """Запускает тесты сравнения скорости итеративных версий."""
    print("СРАВНЕНИЕ СКОРОСТИ: ИТЕРАТИВНЫЕ MERGESORT vs QUICKSORT")
    print("=" * 60)
    
    size = 20000
    
    test_cases = generate_test_cases(size)
    
    for test_name, test_array in test_cases.items():
        print(f"\nТест: {test_name.replace('_', ' ')}")
        print("-" * 40)
        test_iterative_mergesort(test_array)
        test_iterative_quicksort(test_array)
        print("-" * 40)

if __name__ == "__main__":
    run_tests()