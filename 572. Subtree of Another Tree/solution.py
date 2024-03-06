from typing import *

class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, firstTree: Optional[TreeNode], secondTree: Optional[TreeNode]) -> bool:
        """
        Check if two trees are identical.

        Time complexity: O(n), where n is the number of nodes in the tree.
        Space complexity: O(h), where h is the height of the tree.
        """
        if not firstTree and not secondTree:  # If both trees are empty
            return True
        if firstTree and secondTree and firstTree.val == secondTree.val:  # If both trees have the same value at the current node
            return self.isSameTree(firstTree.left, secondTree.left) and self.isSameTree(firstTree.right, secondTree.right)  # Recursively check if the left and right subtrees are identical
        else:
            return False

    def isSubTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Check if a tree is a subtree of another tree.

        Time complexity: O(m * n), where m is the number of nodes in the main tree and n is the number of nodes in the subtree.
        Space complexity: O(h), where h is the height of the main tree.
        """
        if not root:  # If the main tree is empty
            return False
        if self.isSameTree(root, subRoot):  # If the subtree is identical to the main tree
            return True
        return self.isSubTree(root.left, subRoot) or self.isSubTree(root.right, subRoot)  # Recursively check if the subtree is present in the left or right subtree of the main tree
