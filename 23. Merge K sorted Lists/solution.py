from typing import *

class ListNode:
  """
  Represents a node in a linked list.
  """
  def __init__(self, val=0, next=None):
    """
    Initializes a ListNode object.
    - val: The value stored in the node (default 0).
    - next: The next node in the linked list (default None).
    """
    self.val = val
    self.next = next

class Solution:
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merges k sorted linked lists into a single sorted linked list.
    - lists: A list of k sorted linked lists (may be empty).

    Returns the head of the merged linked list, or None if the input list is empty.
    """
    if not lists or len(lists) == 0:
      """
      - Check if the input list is empty (None) or has no elements (length 0).
      - If so, return None to indicate there's nothing to merge.
      """
      return None

    while len(lists) > 1:
      """
      - Continue iterating as long as there are more than one list remaining.
      - This loop merges pairs of lists iteratively until a single merged list remains.
      """
      mergedList = []
      for i in range(0, len(lists), 2):
        """
        - Iterate through the input list in pairs (i, i+1).
        - This loop processes two lists at a time for merging.
        """
        list1 = lists[i]
        list2 = lists[i + 1] if i + 1 < len(lists) else None
        """
        - Access the current and next list in the pair.
        - If there's no next list (i+1 is out of bounds), set it to None.
        """
        mergedList.append(self.mergeSortedLists(list1, list2))
        """
        - Merge the current pair of lists and append the result to a temporary list.
        """
      lists = mergedList
      """
      - Update the input list with the merged results from each iteration.
      - This effectively replaces pairs of lists with their merged counterpart.
      """

    return lists[0]

  def mergeSortedLists(self, list1, list2):
    """
    Merges two sorted linked lists into a single sorted linked list.
    - list1: The first sorted linked list.
    - list2: The second sorted linked list (may be None).

    Returns the head of the merged linked list.
    """
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
      """
      - Iterate as long as both lists have elements.
      - This loop compares the head nodes of both lists and adds the smaller one to the merged list.
      """
      if list1.val < list2.val:
        tail.next = list1
        list1 = list1.next
      else:
        tail.next = list2
        list2 = list2.next
      tail = tail.next

    if list1:
      tail.next = list1
    if list2:
      tail.next = list2

    return dummy.next
