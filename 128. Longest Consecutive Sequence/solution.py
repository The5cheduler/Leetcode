from typing import List

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    numsSet = set(nums)
    longestSequence = 0

    for num in numsSet:
      if (num - 1) not in numsSet:
        continue
      currentSequence = 1
      while (num + 1) in numsSet:
        num += 1
        currentSequence += 1
      longestSequence = max(currentSequence, longestSequence)

      if longestSequence = len(numsSet):
        return longestSequence
    return longestSequence.

  
