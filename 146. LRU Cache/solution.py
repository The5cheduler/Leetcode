class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None  # Previous node in the doubly linked list
        self.next = None  # Next node in the doubly linked list

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key-value pairs and corresponding nodes
        # Doubly linked list sentinel nodes for efficient insertion and removal
        self.left = Node(0, 0)  # Leftmost node (dummy)
        self.right = Node(0, 0)  # Rightmost node (dummy)
        self.left.next, self.right.prev = self.right, self.left  # Connect sentinels

    def get(self, key: int) -> int:
        """Retrieves the value associated with a key, moving the accessed node to the front to prioritize it.

        Args:
            key: The key to search for.

        Returns:
            The value associated with the key, or -1 if not found.
        """

        if key in self.cache:
            node = self.cache[key]
            self.remove(node)  # Detach the node from its current position
            self.insert(node)  # Insert the node at the front (most recently used)
            return node.val
        return -1

    def remove(self, node: Node) -> None:
        """Removes a node from the doubly linked list, maintaining the order.

        Args:
            node: The node to remove.
        """

        previous, next = node.prev, node.next
        previous.next = next
        next.prev = previous

    def insert(self, node: Node) -> None:
        """Inserts a node at the front (most recently used) position of the doubly linked list.

        Args:
            node: The node to insert.
        """

        previous, next = self.right.prev, self.right  # Get the rightmost node (before sentinel)
        previous.next = node
        next.prev = node
        node.prev = previous
        node.next = next

    def put(self, key: int, value: int) -> None:
        """Updates or inserts a key-value pair, potentially removing the least recently used item if capacity is reached.

        Args:
            key: The key to store.
            value: The value to associate with the key.
        """

        if key in self.cache:
            self.remove(self.cache[key])  # Remove the existing node, if any

        node = Node(key, value)  # Create a new node
        self.cache[key] = node  # Add the node to the dictionary
        self.insert(node)  # Insert the node at the front (most recently used)

        if len(self.cache) > self.capacity:  # Eviction if exceeding capacity
            # Remove the least recently used (LRU) node from the linked list and dictionary
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]