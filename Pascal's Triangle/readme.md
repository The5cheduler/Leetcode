# Pascal's Triangle

Given an integer `numRows`, return the first `numRows` of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

## Example

**Example 1:**

Input: `numRows = 5`

Output: `[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]`

**Example 2:**

Input: `numRows = 1`

Output: `[[1]]`

This Python code generates the first `n` rows of Pascal's triangle and prints them to the console. 

## Brute-Force Code Explanation

The function `nCr(n, r)` calculates the binomial coefficient "n choose r" using the formula `n! / (r! * (n-r)!)`. This is used to calculate the values in each row of Pascal's triangle.

## Step-by-Step Explanation

1. Define a function `nCr(n, r)` that calculates the binomial coefficient "n choose r" using the formula `n! / (r! * (n-r)!)`. This function takes two arguments, `n` and `r`, and returns an integer value.

2. Define a function `printPascal(n:int)` that generates the first `n` rows of Pascal's triangle and returns them as a list of lists. This function takes one argument, `n`, and returns a list of lists.

3. Create an empty list called `result` to store the final result.

4. Iterate over each row of the triangle using a `for` loop that ranges from 1 to `n+1`.

5. Create an empty list called `tempLst` to store the values of the current row.

6. Iterate over each column of the current row using a nested `for` loop that ranges from 0 to `row-1`.

7. Append the binomial coefficient of the current row and column to `tempLst` using the `nCr()` function.

8. Append `tempLst` to `result`.

9. Return `result`.

10. In the `if __name__ == '__main__':` block, set `n` to 4.

11. Call the `printPascal()` function with `n` as an argument and store the result in `result`.

12. Iterate over each row of `result` using a `for` loop.

13. Iterate over each value in the current row using a nested `for` loop.

14. Print the current value to the console using the `print()` function.

15. Print a newline character to the console using the `print()` function.
