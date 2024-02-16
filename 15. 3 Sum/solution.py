from typing import List

class solution:
    def threesum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for index, currNum in enumerate(nums):
            if index > 0 and currNum == nums[index]:
                continue

            leftPointer, rightPointer = index + 1, len(nums) - 1
            while leftPointer < rightPointer:
                threeSum = currNum + nums[leftPointer] + nums[rightPointer]
                if threeSum > 0:
                    rightPointer -= 1
                elif threeSum < 0:
                    leftPointer += 1
                else:
                    result.append([currNum, leftPointer, rightPointer])
                    leftPointer += 1
                    while nums[leftPointer] == nums[leftPointer - 1] and leftPointer < rightPointer:
                        leftPointer += 1
        return result