from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []  # Initialize an empty list to store the subsets

        subset = []  # Initialize an empty list to store the current subset

        def backtrack(idx):
            if idx >= len(nums):  # Base case: if the index is out of range, add the current subset to the result
                result.append(subset.copy())
                return
            
            subset.append(nums[idx])  # Include the current number in the subset
            backtrack(idx + 1)  # Recursively call backtrack for the next index

            subset.pop()  # Exclude the current number from the subset
            backtrack(idx + 1)  # Recursively call backtrack for the next index
        
        backtrack(0)  # Start the backtracking process from index 0

        return result  # Return the list of subsets

