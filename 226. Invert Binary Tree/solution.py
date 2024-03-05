from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Check if root is valid
        if not root:
            return None

        # Swap the children
        root.left, root.right = root.right, root.left

        # Make recursive call to children of left
        self.invertTree(root.left)
        self.invert(root.right)

        # return root
        return root