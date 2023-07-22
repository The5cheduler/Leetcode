# Maximum Subarray Sum

Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

## Example

### Example 1

Input: `nums = [-2,1,-3,4,-1,2,1,-5,4]`
Output: `6`
Explanation: The subarray `[4,-1,2,1]` has the largest sum `6`.

### Example 2

Input: `nums = [1]`
Output: `1`
Explanation: The subarray `[1]` has the largest sum `1`.

### Example 3

Input: `nums = [5,4,-1,7,8]`
Output: `23`
Explanation: The subarray `[5,4,-1,7,8]` has the largest sum `23`.

## Constraints

- 1 <= `nums.length` <= 105
- -104 <= `nums[i]` <= 104

## Follow-up

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

## Solution

To solve this problem, we can use Kadane's algorithm, which provides an efficient O(n) solution for finding the maximum subarray sum. Here's the code implementation for the solution:

```python
def max_subarray_sum(nums):
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum
```

For the divide and conquer approach, it's a bit more complex, but it's also more subtle and can be implemented as follows:

```python
def max_subarray_sum_divide_conquer(nums):
    if len(nums) == 1:
        return nums[0]

    mid = len(nums) // 2

    left_max = max_subarray_sum_divide_conquer(nums[:mid])
    right_max = max_subarray_sum_divide_conquer(nums[mid:])
    cross_max = max_crossing_sum(nums, mid)

    return max(left_max, right_max, cross_max)

def max_crossing_sum(nums, mid):
    left_sum = float('-inf')
    right_sum = float('-inf')
    current_sum = 0

    for i in range(mid - 1, -1, -1):
        current_sum += nums[i]
        left_sum = max(left_sum, current_sum)

    current_sum = 0
    for i in range(mid, len(nums)):
        current_sum += nums[i]
        right_sum = max(right_sum, current_sum)

    return left_sum + right_sum
```

Both functions `max_subarray_sum` and `max_subarray_sum_divide_conquer` will give you the maximum subarray sum for the given input array `nums`, depending on which approach you choose to use.