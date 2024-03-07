import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Choose a random pivot from the list
        pivot = random.choice(nums)

        # Partition the list into three parts
        numbers_greater_than_pivot = [x for x in nums if x > pivot]
        numbers_equal_to_pivot = [x for x in nums if x == pivot]
        numbers_less_than_pivot = [x for x in nums if x < pivot]

        # Calculate the lengths of the parts
        len_greater = len(numbers_greater_than_pivot)
        len_equal = len(numbers_equal_to_pivot)

        # If k is less than or equal to the length of the left part,
        # the kth largest number is in the left part
        if k <= len_greater:
            return self.findKthLargest(numbers_greater_than_pivot, k)
        # If k is greater than the length of the left part but less than or equal to
        # the sum of the lengths of the left and middle parts,
        # the kth largest number is equal to the pivot
        elif k <= len_greater + len_equal:
            return pivot
        # Otherwise, the kth largest number is in the right part
        else:
            return self.findKthLargest(numbers_less_than_pivot, k - len_greater - len_equal)