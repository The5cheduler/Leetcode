import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Choose a random pivot element
        pivot = random.choice(nums)

        # Partition the array into three parts: elements less than pivot, elements equal to pivot, elements greater than pivot
        left_half = [x for x in nums if x < pivot]
        middle = [x for x in nums if x == pivot]
        right_half = [x for x in nums if x > pivot]

        # Calculate the lengths of the right_half and middle arrays
        len_right = len(right_half)
        len_middle = len(middle)

        # Recursively find the kth largest element in the right_half or left_half
        if k <= len_right:
            return self.findKthLargest(right_half, k)
        # If k is between len_right and len_right + len_middle, then the pivot is the kth largest element
        elif k <= len_right + len_middle:
            return pivot
        # Recursively find the kth largest element in the left_half
        else: 
            return self.findKthLargest(left_half, k - len_right - len_middle)