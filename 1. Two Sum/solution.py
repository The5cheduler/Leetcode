class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create hash map to store complements and its indecies
        complement = {}

        for i, value in enumerate(nums):
            # check if current value already exists in the complement dictionary
            if value in complement:
                # return current index and value from complement dictionary
                return [i, complement[value]]
            # set complement value as key and index as value
            complement[target - value] = i

        previousMap = {}

        for index in range(len(nums)):
            complement  = target - nums[index]
            if complement in previousMap:
                return [previousMap[complement], index]
            previousMap[nums[index]] = index
            
