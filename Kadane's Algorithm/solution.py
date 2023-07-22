from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_so_far =nums[0]
        curr_max = nums[0]
     
        for i in range(1,len(nums)):
            curr_max = max(nums[i], curr_max + nums[i])
            max_so_far = max(max_so_far,curr_max)
         
        return max_so_far