# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The problem involves finding the top K frequent elements in an array. One approach to solving this is to count the occurrences of each element and then organize them by frequency. The goal is to identify the K most frequent elements.
# Approach
<!-- Describe your approach to solving the problem. -->
The approach involves using a dictionary (count) to store the number of occurrences of each value in the input array (nums). We then use another array (freq) to organize the elements based on their frequencies. After counting the occurrences, we iterate through the count dictionary and append elements to the frequency array, grouping them by their counts.

Finally, we iterate through the frequency array in reverse order, starting from the maximum frequency. We append elements to the result array until we reach the desired K elements. The result array contains the top K frequent elements.
# Complexity
- Time complexity:
    The time complexity is determined by the two passes through the input array and the loop over the frequency array. Therefore, the time complexity is O(n), where n is the length of the input array (nums).
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
  The space complexity is influenced by the storage of counts and the frequency array. Since the frequency array can have at most n + 1 elements (each frequency from 0 to n), the space complexity is O(n).
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # defined store number of occurance of value
        count = {}
        # empty arrays to store the frequency an its number
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)
        
        result = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
```
