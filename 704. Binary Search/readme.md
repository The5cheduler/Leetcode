Python
```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + (high - low) // 2)  # Keep the original midpoint calculation

            # Adjust conditions based on midpoint calculation
            if mid < 0 or mid >= len(nums):  # Handle potential out-of-bounds issue
                return -1
            elif nums[mid] == target:
                return mid
            elif nums[mid] > target and mid > 0:  # Check for valid index before comparison
                high = mid - 1
            else:
                low = mid + 1

        return -1  # Target not found

```