from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')  # Initialize the maximum sum to negative infinity

        def depth_first_search(node):
            nonlocal max_sum  # Use the nonlocal keyword to access the max_sum variable from the outer scope

            if not node:  # If the node is None, return 0
                return 0
            
            # Recursively calculate the maximum sum of the left and right subtrees
            left_max = max(depth_first_search(node.left), 0)
            right_max = max(depth_first_search(node.right), 0)

            # Update the max_sum if the current path sum is greater
            max_sum = max(max_sum, left_max + right_max + node.val)

            # Return the maximum sum of the current node and either the left or right subtree
            return max(left_max, right_max) + node.val
        
        depth_first_search(root)  # Start the depth-first search from the root node
        return max_sum  # Return the maximum sum
