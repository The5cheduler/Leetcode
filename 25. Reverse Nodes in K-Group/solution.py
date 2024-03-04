from typing import *

class ListNode:
    def __init__(self, val=0, next=0) -> None:
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       # Create a dummy node to simplify linking and handle potential head changes
       dummy = ListNode(0, head)  # Create a dummy node before the head
       group_prev = dummy  # Pointer to the start of the current group to be reversed

       # Iterate until there aren't enough nodes for a group of k
       while True:
            kth_node = self.getKth(group_prev, k)  # Find the kth node from the current group
            if not kth_node:  # If we don't have a kth node, we're done
                break

            group_next = kth_node.next  # Mark the beginning of the next group

            # Reverse the current group of k nodes
            previous, current = kth_node.next, group_prev.next  # Initialize pointers for reversal
            while current != group_next:
                temp = current.next  # Store the next node for later
                current.next = previous  # Reverse the link
                previous = current  # Move pointers forward
                current = temp

            # Connect the reversed group with the previous and next groups
            temp = group_prev.next  # Store the first node of the reversed group
            group_prev.next = kth_node  # Connect the previous group with the new tail
            group_prev = temp  # Move the group_prev pointer to the beginning of the next group

       return dummy.next  # Return the head of the modified linked list (excluding the dummy)

    # Helper function to find the kth node from a given node
    def getKth(self, current, k):
        while current and k > 0:  # Traverse k nodes forward
            current = current.next
            k -= 1
        return current  # Return the kth node (or None if not enough nodes)