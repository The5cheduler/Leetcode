class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Initialize a TreeNode object with a value and left and right child nodes.
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def depth_first_search(node, max_value):
            # Perform a depth-first search on the binary tree to count the number of good nodes.
            if not node:
                return 0
            result = 1 if node.val >= max_value else 0
            # Increment the result if the current node's value is greater than or equal to the maximum value encountered so far.
            max_value = max(max_value, node.val)
            # Update the maximum value encountered so far.
            result += depth_first_search(node.left, max_value)
            # Recursively call the depth_first_search function on the left child node.
            result += depth_first_search(node.right, max_value)
            # Recursively call the depth_first_search function on the right child node.
            return result
        return depth_first_search(root, root.val)