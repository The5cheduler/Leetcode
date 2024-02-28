# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

**Imagine you have two sorted lines of people:**

1. **Compare individuals:** Start by comparing the first person from each line.
2. **Add the smaller:** Add the person with the **smaller value** to a **new line** (merged list).
3. **Move the shorter line:** Move the **pointer** in the line that just contributed a person **forward one position**.
4. **Repeat:** Keep comparing and adding people until one line is empty.
5. **Append the remaining:** Add all the remaining people from the **non-empty line** to the end of the merged list.

**Key points:**

* We don't create a completely new list; instead, we build the merged list step-by-step by comparing and adding individuals.
* This approach works because both original lists are already sorted.
* We keep track of the position in each list using pointers.

# Approach
<!-- Describe your approach to solving the problem. -->

1. **Initialize:** Create a dummy node and set its `next` to the head of the merged list.
2. **Traverse:** While both lists have nodes:
    - Compare the heads of each list.
    - Append the smaller node to the tail's `next`.
    - Update the tail to point to the appended node.
3. **Append remaining nodes:** Append any remaining nodes from either list to the tail's `next`.
4. **Return:** Return the dummy node's `next`, which is the head of the merged list.


# Complexity
- Time complexity: $$O(m + n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
This is because the algorithm iterates through both linked lists (list1 and list2) with a combined length of m + n, comparing and appending nodes at each step.

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The algorithm only uses constant additional space for temporary variables (dummy node, tail pointer, and comparison variables). It doesn't allocate any extra memory based on the input size (m and n).

# Code
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
        
```
