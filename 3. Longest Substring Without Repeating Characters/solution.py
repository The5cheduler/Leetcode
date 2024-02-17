class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characterSet = set()
        leftPointer = 0
        result = 0

        for rightPointer in range(len(s)):
            while s[rightPointer] in characterSet:
                characterSet.remove(s[leftPointer])
                leftPointer += 1
            characterSet.add(s[rightPointer])
            result = max(result, rightPointer - leftPointer + 1)
        return result