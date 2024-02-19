from typing import List

class Solution:
    def generateParanthesis(self, n: int) -> List[str]:
        #  create the stack to store the current valid parentheses combination
        stack = []
        # Create the result variable to store all possible valid parathesis combinations for given number
        result = []

        # Define backtracking function which will find generate valid parentheses
        def backTrack(openCount: int, closeCount: int):
            # base case if number of open brackets count is same as given number and closed brackets count that means we have found the valid parentheses
            if openCount == closeCount == n:
                result.append("".join(stack)) # append the current stack value to result
                return # return to the last method callout

            # we can only add open bracket if open brackets count is lower than given number
            if openCount < n:
                stack.append("(") # add open bracket to stack
                backTrack(openCount + 1, closeCount) # make call to method with new updated value until it does not qualify for the condition
                stack.pop() # clean up the stack once

            # We can only add the closed bracket if closed bracket count is less than open bracket count
            if closeCount < openCount:
                stack.append(")") # add closed bracket to stack
                backTrack(openCount, closeCount + 1) # update the closed bracket count and call backTrack again
                stack.pop() # clean up once done with all backtracking.

        # make call to backTrackFunction
        backTrack(0, 0)
        return result