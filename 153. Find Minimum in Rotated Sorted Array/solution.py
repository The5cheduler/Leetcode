from typing import List
class Solution:
  def findMin(self, nums: List[int]) -> int:
    # Handle unrotated Array
    if nums[0] < num[-1]:
      return nums[0]

    # Define two pointer left and right
    left, right = 0, len(nums) - 1
    while left < right:
      mid = left + (right - left) // 2

      # We need to check only right side of the Array
      # As rotated elements will be on that side only
      # Check if mimimum value lies in to right sub array
      if nums[mid] > nums[right]:
        left = mid + 1 # If condition satisfies, update the left value to mid + 1 as we know for sure left sub array contain value that are bigger
      else:
        right = mid # Else update the right pointer's value to be mid as minimum lies between left and mid
    return nums[left]
