# Define a class TreeNode to represent a node in a binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Import the deque class from the collections module
from collections import deque

# Import the List and Optional classes from the typing module
from typing import List, Optional

# Define a class Solution to solve the problem
class Solution:
    # Define a method levelOrder to perform level order traversal on a binary tree
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Initialize an empty list to store the result
        result = []

        # Initialize a deque to store the nodes of the current level
        nodes = deque()

        # Append the root node to the deque
        nodes.append(root)

        # Perform level order traversal
        while nodes:
            # Initialize an empty list to store the values of the nodes in the current level
            sub_nodes = []

            # Get the number of nodes in the current level
            node_length = len(nodes)

            # Process each node in the current level
            for i in range(node_length):
                # Remove the leftmost node from the deque
                node = nodes.popleft()

                # If the node is not None, add its value to the sub_nodes list
                # and append its left and right child nodes to the deque
                if node:
                    sub_nodes.append(node.val)
                    nodes.append(node.left)
                    nodes.append(node.right)

            # If the sub_nodes list is not empty, append it to the result list
            if sub_nodes:
                result.append(sub_nodes)

        # Return the result list
        return result