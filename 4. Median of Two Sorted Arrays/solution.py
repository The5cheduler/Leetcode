from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Finds the median of two sorted arrays.

        Args:
            nums1: The first sorted list of integers.
            nums2: The second sorted list of integers.

        Returns:
            The median of the combined sorted array.
        """

        # Assign input lists to descriptive variables for clarity
        n1_length, n2_length = len(nums1), len(nums2)

        # Ensure sorted_list_a is always the shorter list for efficient searching
        if n1_length > n2_length:
            return self.findMedianSortedArrays(nums2, nums1)

        # Calculate total elements and half elements for median calculation
        total_elements = n1_length + n2_length
        left = (n1_length + n2_length + 1) // 2

        # Initialize variables for binary search
        low, high = 0, n1_length

        while low <= high:
            # Calculate indices for potential median elements in both lists
            index_a = (low + high) // 2
            index_b = left - index_a

            # Handle potential out-of-bounds cases with infinity
            nums1_left = nums1[index_a - 1] if (index_a - 1) >= 0 else float("-infinity")
            nums1_right = nums1[index_a] if (index_a) < n1_length else float("infinity")
            nums2_left = nums2[index_b - 1] if (index_b - 1) >= 0 else float("-infinity")
            nums2_right = nums2[index_b] if (index_b) < n2_length else float("infinity")

            # Check if potential median elements are in correct positions
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # Calculate median based on odd or even number of elements
                if total_elements % 2:
                    return max(nums1_left, nums2_left)  # Median is the middle element
                else:
                    return (float(max(nums1_left, nums2_left)) + float(min(nums1_right, nums2_right))) / 2.0  # Median is the average of middle two elements

            elif nums1_left > nums2_right:  # Adjust search space towards smaller elements
                high = index_a - 1
            else:  # Adjust search space towards larger elements
                low = index_a + 1
        return 0
