from typing import Optional

class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def reverse(self, head: Optional[Node]) -> Optional[Node]:
        # Define Pointer to None
        previous = None
        # Set current pointer with head value
        current = head

        while current:
            # define next and assign ito current.next
            next = current.next
            # set previous pointer to current.next
            current.next = previous
            # set current to previous
            previous = current
            # set next to current
            current = next
        return previous