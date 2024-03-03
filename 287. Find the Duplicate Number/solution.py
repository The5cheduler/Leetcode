from typing import *

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Initialize two pointers: slow_pointer and fast_pointer.
        slow_pointer = 0
        fast_pointer = 0

        # Use Floyd's Cycle Finding Algorithm (also known as Tortoise and Hare Algorithm)
        while True:
            # Slow pointer moves one step forward at a time.
            slow_pointer = nums[slow_pointer]

            # Fast pointer moves two steps forward at a time.
            fast_pointer = nums[nums[fast_pointer]]  # Dereference the value at fast_pointer first

            # If slow and fast pointers meet, a cycle exists, indicating a duplicate.
            if slow_pointer == fast_pointer:
                break

        # Reset one pointer (slow_pointer) to the beginning of the list.
        second_slow_pointer = 0

        # Move both pointers one step at a time until they meet.
        while True:
            slow_pointer = nums[slow_pointer]
            second_slow_pointer = nums[second_slow_pointer]

            # When they meet, the point of intersection is the duplicate number.
            if slow_pointer == second_slow_pointer:
                return slow_pointer

