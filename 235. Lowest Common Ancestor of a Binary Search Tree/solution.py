from typing import *

class TreeNode:
    def __init__(self, val = 0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        current = root  # Initialize a variable 'current' with the root node

        while root:  # Loop until 'root' is not None
            if p.val > current.val and q.val > current.val:  # If both p and q are greater than current node's value
                current = current.right  # Move to the right child
            elif p.val < current.val and q.val < current.val:  # If both p and q are less than current node's value
                current = current.left  # Move to the left child
            else:
                return current  # If neither of the above conditions are met, current node is the lowest common ancestor
