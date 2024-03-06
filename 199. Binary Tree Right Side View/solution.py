from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Value of the node
        self.left = left  # Left child of the node
        self.right = right  # Right child of the node

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []  # List to store the right side view of the binary tree
        nodes = deque([root])  # Queue to store the nodes of the current level

        while nodes:
            right_node = None  # Variable to store the rightmost node of the current level
            queue_length = len(nodes)  # Number of nodes in the current level

            for i in range(queue_length):
                node = nodes.popleft()  # Get the next node from the queue
                if node:
                    right_node = node  # Update the rightmost node
                    nodes.append(node.left)  # Add the left child to the queue
                    nodes.append(node.right)  # Add the right child to the queue

            if right_node:
                result.append(right_node.val)  # Add the value of the rightmost node to the result list

        return result  # Return the right side view of the binary tree
