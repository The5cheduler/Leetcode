from typing import List

class solution:
    def containsDuplicate(nums: List[int]) -> bool:
        map = set()
        for value in nums:
            if value in map:
                return True
            map.add(value)
        return False


if __name__ == "__main__":
    print(solution.containsDuplicate(nums=[1,2,3]))
