from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary to store the count of each number
        count = {}

        # List of empty arrays to store numbers based on their frequency
        freq = [[] for i in range(len(nums) + 1)]

        # Count the occurrences of each number in the input list
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Populate the frequency list with numbers based on their occurrence count
        for n, c in count.items():
            freq[c].append(n)
        
        # Result list to store the final output
        result = []

        # Traverse the frequency list in reverse order
        for i in range(len(freq) - 1, 0, -1):
            # Traverse the numbers at each frequency
            for n in freq[i]:
                # Append the number to the result list
                result.append(n)
                # Check if we have found k numbers, if yes, return the result
                if len(result) == k:
                    return result
