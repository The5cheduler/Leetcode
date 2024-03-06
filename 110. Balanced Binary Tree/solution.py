from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self, root: Optional[TreeNode]) -> bool:
        # Define a helper function for depth-first search
        def depth_first_search(root):
            # Base case: if root is None, return [True, 0]
            if not root:
                return [True, 0]

            # Recursively call depth_first_search on left and right subtrees
            left = depth_first_search(root.left)
            right = depth_first_search(root.right)

            # Check if the current subtree is balanced
            balance = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            # Return the balance status and the maximum depth of the subtree
            return [balance, 1 + max(left[1], right[1])]

        # Call depth_first_search on the root and return the balance status
        return depth_first_search(root)[0]