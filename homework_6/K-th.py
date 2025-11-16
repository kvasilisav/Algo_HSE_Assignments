import random
from typing import List

def find_kth_largest(nums: List[int], k: int) -> int:
    target_index = len(nums) - k
    
    def partition(left: int, right: int, pivot_index: int) -> int:
        pivot_value = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        store_index = left
        
        for i in range(left, right):
            if nums[i] < pivot_value:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
                
        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index
    
    def select(left: int, right: int) -> int:
        if left == right:
            return nums[left]
            
        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)
        
        if target_index == pivot_index:
            return nums[pivot_index]
        elif target_index < pivot_index:
            return select(left, pivot_index - 1)
        else:
            return select(pivot_index + 1, right)
    
    return select(0, len(nums) - 1)

# Тесты
assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
assert find_kth_largest([1], 1) == 1
assert find_kth_largest([1, 2, 3, 4, 5], 1) == 5
assert find_kth_largest([5, 4, 3, 2, 1], 5) == 1
assert find_kth_largest([-5, -10, -3, -1, -7], 2) == -3
assert find_kth_largest([7, 7, 7, 7, 7], 3) == 7