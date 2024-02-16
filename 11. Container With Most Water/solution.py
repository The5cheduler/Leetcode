from typing import List

class solution:
    def maxArea(self, height: List[int]) -> int:
        leftPointer, rightPointer = 0 , len(height) - 1
        maxWaterStorage = 0

        while leftPointer < rightPointer:
            currentWaterStorage = ((rightPointer - leftPointer) * min(height[leftPointer], height[rightPointer]))
            maxWaterStorage = max(currentWaterStorage, maxWaterStorage)

            if height[leftPointer] < height[rightPointer]:
                leftPointer += 1
            else:
                rightPointer -= 1
        return maxWaterStorage