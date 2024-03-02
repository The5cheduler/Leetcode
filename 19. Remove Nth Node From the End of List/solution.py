from typing import *

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to simplify edge case ( when removing the head)
        dummyNode = ListNode(0, head)
        fast = head
        slow = dummyNode

        # Adcance the fast pointer to n positions ahead of slow pointer
        while n > 0 and fast:
            fast = fast.next # Move fast pointer by one
            n -= 1 # Decreament n for each fast pointer has moved ahead

        # Traverse together until fast pointer reaches the end
        while fast:
            fast = fast.next # Move fast pointer by one step
            slow = slow.next # Move slow pointer by one step

        # Once Fast pointer reaches end slow pointer is pointing at the node before the node to be removed
        slow.next = slow.next.next #Remove the nth node from the LinkedList by skipping it

        # Returning the head
        return dummyNode.next