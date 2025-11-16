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

def mergesort(arr: List) -> List:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left: List, right: List) -> List:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quicksort(arr: List) -> List:
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quicksort(less) + equal + quicksort(greater)

def generate_reverse_with_min_first(n: int) -> List[int]:
    return [1] + list(range(n, 1, -1))

def generate_sorted_with_max_first(n: int) -> List[int]:
    return [n] + list(range(1, n))

def generate_peak_valley(n: int) -> List[int]:
    result = []
    low, high = 1, n
    for i in range(n):
        result.append(low if i % 2 == 0 else high)
        low += 1 if i % 2 == 0 else 0
        high -= 1 if i % 2 == 1 else 0
    return result

def generate_many_duplicates(n: int) -> List[int]:
    return [random.randint(0, 10) for _ in range(n)]

def generate_cache_friendly(n: int) -> List[int]:
    return [random.randint(0, n) for _ in range(n)]

def generate_test_cases(size: int = 5000) -> dict:
    return {
        'минимальный_первый': generate_reverse_with_min_first(size),
        'максимальный_первый': generate_sorted_with_max_first(size),
        'пик_долина': generate_peak_valley(size),
        'много_дубликатов': generate_many_duplicates(size),
        'рандом': generate_cache_friendly(size),
    }

@timing_decorator
def test_mergesort(arr: List) -> List:
    return mergesort(arr.copy())

@timing_decorator
def test_quicksort(arr: List) -> List:
    return quicksort(arr.copy())

def run_tests():
    print("СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ: MERGESORT vs QUICKSORT")
    print("=" * 50)
    
    test_cases = generate_test_cases(10000)
    
    for test_name, test_array in test_cases.items():
        print(f"\nТест: {test_name.replace('_', ' ')}")
        print("-" * 30)
        test_mergesort(test_array)
        test_quicksort(test_array)
        print("-" * 30)

if __name__ == "__main__":
    run_tests()