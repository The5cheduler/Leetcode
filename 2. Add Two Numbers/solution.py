from typing import *

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = currrent = ListNode()  # Create a dummy head node for the result list

        carry = 0  # Initialize a variable to store the carry over value

        while list1 or list2 or carry:  # Loop until all digits are processed and carry is 0
            total = 0  # Initialize a variable to store the sum of digits and carry

            if list1:  # Add the value from the first list if it exists
                total += list1.val
                list1 = list1.next  # Move to the next node in the first list

            if list2:  # Add the value from the second list if it exists
                total += list2.val
                list2 = list2.next  # Move to the next node in the second list

            total += carry  # Add the carry over from the previous digit

            carry = total // 10  # Calculate the carry over for the next digit
            total %= 10  # Extract the current digit for the sum

            currrent.next = ListNode(total)  # Create a new node for the sum digit
            currrent = currrent.next  # Move the pointer to the newly created node

        return dummy.next  # Return the actual head (excluding the dummy node) of the result list

