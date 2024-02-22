from typing import List

class Solution:
    def serch(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + right // 2

            if nums[mid] == target:
                return mid

            # Check for the left sorted sub array
            if nums[left] <= nums[mid]:
                # Check if target is less than nums[mid] and greater than or equals to target
                if nums[left] <= target < nums[mid]:
                    right = mid - 1 #move the right pointer as target is less than nums[mid]
                else:
                    left = mid + 1 # else move the left pointer
            # Check for right sorted Array
            else:
                # Check if target if greater than nums[mid] and target <= nums[right]
                if nums[mid] > target >= nums[right]:
                    left = mid + 1 # Move the left pointer as target is greater then
                else:
                    right = mid - 1 # Else move tha right pointer.
        return -1