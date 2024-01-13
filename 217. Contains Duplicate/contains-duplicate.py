from typing import List


def containsDuplicate(nums:List[int]) ->  bool:
    hashMap = {}
    for i in range(len(nums)):
        hashMap[nums[i]] = i

    if len(hashMap) < len(nums):
        return True
    return False

if __name__ == "__main__":
    inputValue = [1,1,1,3,3,4,3,2,4,2]
    print(containsDuplicate(nums=inputValue))

