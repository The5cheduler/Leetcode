# Problem: 74. Search 2D matrix

## Problem Description:
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

Implement the `searchMatrix(matrix: List[List[int]], target: int) -> bool` function, which returns `True` if the target value exists in the matrix and `False` otherwise.

## Solution Approach:
To solve this problem, we can use a modified binary search algorithm. We start by treating the 2D matrix as a 1D sorted array. We can calculate the mid index of this 1D array and convert it back to the corresponding row and column indices in the 2D matrix.

Here are the steps for the solution approach:

1. Initialize the `start` and `end` indices of the 1D array as 0 and `m * n - 1` respectively, where `m` is the number of rows and `n` is the number of columns in the matrix.
2. While `start` is less than or equal to `end`, do the following:
   - Calculate the `mid` index as `(start + end) // 2`.
   - Convert the `mid` index to the corresponding row and column indices in the 2D matrix using the formulas:
     - `row = mid // n`
     - `col = mid % n`
   - Compare the value at the calculated indices with the target value:
     - If the value is equal to the target, return `True`.
     - If the value is less than the target, update `start` to `mid + 1`.
     - If the value is greater than the target, update `end` to `mid - 1`.
3. If the target value is not found after the loop, return `False`.

## Complexity Analysis:
- Time Complexity: $$O(log(m + n))$$, where m is the number of rows and n is the number of columns in the matrix.
- Space Complexity: O(1)

## Example:
```python []
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, cols = len(matrix), len(matrix[0])

        first, last = 0, row - 1

        while first <= last:
            row = first + last // 2

            if target > matrix[row][-1]:
                first = row + 1
            elif target < matrix[row][0]:
                last = row - 1
            else:
                break

        row = first + last // 2
        left, right = 0, cols - 1

        while left <= right:
            mid = left + right // 2

            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True

        return False
```
```javascript []
class Solution {
    searchMatrix(matrix, target) {
        let row = matrix.length;
        let cols = matrix[0].length;

        let first = 0;
        let last = row - 1;

        while (first <= last) {
            row = Math.floor((first + last) / 2);

            if (target > matrix[row][cols - 1]) {
                first = row + 1;
            } else if (target < matrix[row][0]) {
                last = row - 1;
            } else {
                break;
            }
        }

        row = Math.floor((first + last) / 2);
        let left = 0;
        let right = cols - 1;

        while (left <= right) {
            let mid = Math.floor((left + right) / 2);

            if (target > matrix[row][mid]) {
                left = mid + 1;
            } else if (target < matrix[row][mid]) {
                right = mid - 1;
            } else {
                return true;
            }
        }

        return false;
    }
}
```
