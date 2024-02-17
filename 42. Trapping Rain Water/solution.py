from typing import List

class solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        leftPointer, rightPointer = 0, len(height) - 1
        maxLeft, maxRight = height[leftPointer], height[rightPointer]
        result = 0

        while leftPointer < rightPointer:
            if maxLeft < maxRight:
                leftPointer += 1
                maxLeft = max(maxLeft, height[leftPointer])
                result += (maxLeft - height[leftPointer])
            else:
                rightPointer -= 1
                maxRight = max(maxRight, height[rightPointer])
                result += (maxRight -  height[rightPointer])

        return result
