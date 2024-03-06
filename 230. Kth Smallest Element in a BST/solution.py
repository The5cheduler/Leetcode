from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []  # Stack to store nodes
        current = root  # Current node

        while stack or current:
            while current:
                stack.append(current)  # Add current node to stack
                current = current.left  # Move to the left child
            current = stack.pop()  # Pop the top node from stack
            k -= 1  # Decrement k
            if k == 0:
                return current.val  # Return the value of kth smallest element
            current = current.right  # Move to the right child
