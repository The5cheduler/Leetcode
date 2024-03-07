from typing import *


# Define a TreeNode class to represent a node in a binary tree
class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

# Define a Solution class to solve the problem
class Solution:
    def buildTree(self, preorder: List[int], inorder:List[int]) -> Optional[TreeNode]:
        # Base case: if either preorder or inorder list is empty, return None
        if not preorder or not inorder:
            return None
        
        if inorder:
            # Get the root value from the preorder list and remove it
            root_val = preorder.pop(0)
            
            # Create a new TreeNode with the root value
            root = TreeNode(root_val)
            
            # Find the index of the root value in the inorder list
            mid_idx = inorder.index(root_val)
            
            # Recursively build the left subtree using the preorder and inorder lists
            root.left = self.buildTree(preorder, inorder[:mid_idx])
            
            # Recursively build the right subtree using the preorder and inorder lists
            root.right = self.buildTree(preorder, inorder[mid_idx + 1:])
            
            # Return the root of the constructed binary tree
            return root

