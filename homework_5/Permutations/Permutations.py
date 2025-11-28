from typing import List
from homework_5.Tracer.tracer import tracer

@tracer
def permute(nums: List[int]) -> List[List[int]]:
    if len(nums) <= 1:
        return [nums.copy()]
    
    result = []
    for i in range(len(nums)):
        current = nums[i]
        remaining = nums[:i] + nums[i+1:]
        for perm in permute(remaining):
            result.append([current] + perm)
    return result

assert len(permute([])) == 1
assert len(permute([1])) == 1
assert len(permute([0, 1])) == 2
assert len(permute([1, 2, 3])) == 6
assert len(permute([1, 2, 3, 4])) == 24
assert len(permute([-1, 0, 1])) == 6
assert len(permute([1, 1, 2])) == 6
