from typing import Optional

# Define a class called TreeNode to represent a node in a binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Initialize the node with a value, and left and right child nodes
        self.val = val
        self.left = left
        self.right = right

# Define a class called Solution
class Solution:
    # Define a method called isValidBST that takes a TreeNode object as input and returns a boolean value
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Define a helper function called isValid that checks if a binary tree is a valid binary search tree
        def isValid(node, left, right):
            # If the current node is None, it means we have reached the end of a branch and it is valid
            if not node:
                return True
            # If the value of the current node is not within the range (left, right), it is not a valid BST
            if not (left < node.val < right):
                return False
            # Recursively check the left and right subtrees, updating the range accordingly
            return isValid(node.left, left, node.val) and isValid(node.right, node.val, right)
        
        # Call the isValid function with the root node and the minimum and maximum possible values for a node
        return isValid(root, float('-inf'), float('inf'))