# Definiation for Singly Linked List
class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # Create a dummy node
    dummy = ListNode()
    tail = dummy

    # Run the comparison only when both list1 and list2 are non-empty
    while list1 and list2:
      # Check if list1's value is greater than list2's value
      if list1.val > list2.val:
        # If greater update the tail pointer to list2
        tail.next = list2
        # update the pointer for current node for list1 to the next  
        list2 = list2.next
      
      # Else list2's value is greater than list1's value
      else:
        # Update the tail pointer to list1's Node
        tail.next =  list1
        # update pointer for current Node to point at next Node
        list1 = list1.next

      # Update the tail pointer
      tail = tail.next

    # Check if list1 or list2 any of the list has remaining node
    if list1:
      tail.next = list1
    elif list2:
      tail.next = list2

    # return the head node which is dummy.next
    return dummy.next
    
        
