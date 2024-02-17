class Solution:
    def characterReplacement(self, s: str, k:int) -> int:
        count = {}
        result, leftPointer = 0, 0

        for rightPointer in range(len(s)):
            count[s[rightPointer]] = 1 + count.get(s[rightPointer], 0)
            currentWindow = rightPointer - leftPointer + 1

            while currentWindow - max(count.values()) > k:
                count[s[leftPointer]] -= 1
                leftPointer += 1
                currentWindow = rightPointer - leftPointer + 1

            result = max(result, currentWindow)
        return result

    def characterReplacement(self, s: str, k: int) -> int:
        count, result, leftPointer, maxFrequency = {}, 0, 0 , 0

        for rightPointer in range(len(s)):
            count[s[rightPointer]] = 1 + count.get(s[rightPointer],0)
            maxFrequency = max(maxFrequency, count[s[rightPointer]])
            currentWindow = (rightPointer - leftPointer + 1)

            while currentWindow - maxFrequency > k:
                count[s[leftPointer]] -= 1
                leftPointer += 1
                currentWindow = rightPointer - leftPointer + 1

            result = max(result, currentWindow)
        return result