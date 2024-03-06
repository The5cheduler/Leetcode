from typing import *

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Check if two binary trees are identical.

        Time complexity: O(n), where n is the number of nodes in the tree.
        Space complexity: O(h), where h is the height of the tree.
        """
        # If both trees are empty, they are identical
        if not p and not q:
            return True

        # If both trees are non-empty and have the same root value,
        # recursively check if their left and right subtrees are identical
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            # If any of the above conditions fail, the trees are not identical
            return False
