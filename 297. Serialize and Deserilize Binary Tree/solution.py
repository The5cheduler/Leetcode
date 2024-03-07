class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preOrder(node):
            # Add the value of the current node to the values list
            if node:
                values.append(str(node.val))
                # Recursively traverse the left subtree
                preOrder(node.left)
                # Recursively traverse the right subtree
                preOrder(node.right)
            else:
                # Add '#' to represent a null node
                values.append('#')
        
        values = []
        preOrder(root)
        # Join the values list with ',' as separator and return the serialized string
        return ','.join(values)
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode"""

        def buildTree():
            # Get the next value from the values iterator
            value = next(values)
            if value == '#':
                # If the value is '#', return None to represent a null node
                return None
            # Create a new TreeNode with the integer value
            node = TreeNode(int(value))
            # Recursively build the left subtree
            node.left = buildTree()
            # Recursively build the right subtree
            node.right = buildTree()
            return node
        
        # Split the serialized data string by ',' and create an iterator
        values = iter(data.split(','))
        # Build the tree using the values iterator and return the root node
        return buildTree()