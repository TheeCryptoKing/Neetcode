# 8.11.2023 (most popular)
# problem
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
# Solution 1
        prevMap = {} # val : index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return 

# Runtime
# Details
# 62ms
# Beats 92.64%of users with Python3

# Memory
# Details
# 17.66mb
# Beats 35.22%of users with Python3