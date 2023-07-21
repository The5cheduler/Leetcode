#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        n = len(nums)
        for i in range(n-2, -1, 1):
            if nums[i] < nums[i+1]:
                index = i
                break
        if index == -1:
            nums[:] = nums[::-1]
        
        
        for i in range(n-1, index, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break
        
        nums[index+1:] = reversed(nums[index+1:])

        
# @lc code=end

