from typing import *

class Node:
    def __init__(self, x:int, next:'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            """
            Handle the base case: if the original list is empty, return None
            """
            return None

        current_node = head
        while current_node:
            """
            1. Iterate through the original list:
                - Create a new node with same values as current_node
                - Insert the new node **after** the current node by setting the current node's `next` pointer to the new node.
                - Advance the `current_node` pointer to point to the newly inserted node.
            """
            new_node = Node(current_node.val, current_node.next)
            current_node.next = new_node
            current_node = new_node.next

        current_node = head
        while current_node:
            """
            2. Assign random pointers in the copied list:
                - If the current node in the original list has a random pointer,
                  set the random pointer of the corresponding copy node to the next node of the original random pointer's copy.
                - Advance the `current_node` pointer to iterate through the original list.
            """
            if current_node.random:
                current_node.next.random = current_node.random.next
            current_node = current_node.next.next

        old_head = head
        new_head = head.next
        old_current_node = old_head
        new_current_node = new_head

        while old_current_node:
            """
            3. Separate the original and copied lists:
                - Restore the original list by skipping every other node (keeping only the original nodes).
                - Restore the `next` pointers in the copied list by skipping every other node (keeping only the copied nodes).
                - Advance both the original and copied list pointers.
            """
            old_current_node.next = old_current_node.next.next
            new_current_node.next = new_current_node.next.next if new_current_node.next else None
            old_current_node = old_current_node.next
            new_current_node = new_current_node.next

        return new_head