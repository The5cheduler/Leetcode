from typing import *

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = currrent = ListNode()

        carry = 0
        while list1 or list2 or carry:
            total = 0
            if list1:
                total += list1.val
            if list2:
                total += list2.val
            if carry:
                total += carry

            carry = total // 10
            total %= 10

            currrent.next = ListNode(total)
            currrent = currrent.next

            if list1:
                list1 = list1.next
            if list2:
                list2 = list2.next
        return dummy.next

