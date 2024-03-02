from typing import *

class ListNode:
    def __init__(self, val= 0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def reorderList(seld, head: Optional[ListNode]) ->None:

        # 1. Find the middle node:
        #   - Use two pointers, 'slow' and 'fast'.
        #   - 'slow' moves one step at a time, while 'fast' moves two steps at a time.
        #   - When 'fast' reaches the end or the second to last node (fast.next is None or fast.next.next is None),
        #     'slow' will be at the middle node.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half of the list:
        #   - Start from the middle node (`slow.next`) and traverse the second half.
        #   - Use a temporary variable `previous` to store the previous node.
        #   - For each node in the second half:
        #     - Store the next node (`next_node`) in a temporary variable.
        #     - Set the current node's `next` pointer to point to the previous node.
        #     - Update the previous node and the current node for the next iteration.
        second_half = slow.next
        previous = slow.next = None
        while second_half:
            next_node = second_half.next
            second_half.next = previous
            previous = second_half
            second_half = next_node


        # 3. Merge the first and second halves:
        #   - Start from the head (`first_half`) and the reversed second half (`previous`).
        #   - Iterate until `second_half` is not None:
        #     - Store the next nodes of the first and second halves in temporary variables (`next_first` and `next_second`).
        #     - Connect the first half node to the second half node (`first_half.next = second_half`).
        #     - Connect the second half node to the next node of the first half (`second_half.next = next_first`).
        #     - Update the pointers for the next iteration (`first_half = next_first`, `second_half = next_second`).
        first_half, second_half = head, previous
        while second_half:
            next_first, next_second = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = next_first
            first_half, second_half = next_first, next_second