from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Initialize the maximum area to 0
        maxArea = 0
        # Create an empty stack to store indices and heights
        stack = []

        # Loop through each index and height in the heights list
        for index, height in enumerate(heights):
            # Start with the current index
            start = index
            # Check if the stack is not empty and the height of the current bar is less than the height of the bar at the top of the stack
            while stack and stack[-1][1] > height:
                # Pop the index and height of the bar from the stack
                index_popped, height_popped = stack.pop()
                # Calculate the area of the rectangle formed by the popped bar
                # The width of the rectangle is the difference between the current index and the index of the popped bar
                # The height of the rectangle is the height of the popped bar
                area = height_popped * (index - index_popped)
                # Update the maximum area
                maxArea = max(maxArea, area)
                # Update the start index to the index of the popped bar
                start = index_popped
            # Push the current index and height onto the stack
            stack.append((start, height))

        # Process the remaining bars in the stack
        # Each bar in the stack represents a rectangle with width equal to the number of bars remaining to the right of it
        for i, h in stack:
            # Calculate the area of the rectangle formed by the remaining bar
            # The width of the rectangle is the difference between the total number of bars and the index of the remaining bar
            # The height of the rectangle is the height of the remaining bar
            area = h * (len(heights) - i)
            # Update the maximum area
            maxArea = max(maxArea, area)

        # Return the maximum area
        return maxArea
