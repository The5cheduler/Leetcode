from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams together from a given list of strings.

        Args:
            strs (List[str]): The list of strings to group anagrams from.

        Returns:
            List[List[str]]: A list of lists, where each inner list contains a group of anagrams.

        Time complexity: O(NK) as we traverse through N strings of length K.
        Space complexity: O(NK) as we store N strings of length K.
        """
        # store the results in the default dictionary to handle single value list
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26  # for a .. z
            for c in s:
                # create count list with number
                count[ord(c) - ord("a")] += 1
            # map it back to results dictionary with string (it will be stored as list as we have defined default value to be list)
            result[tuple(count)].append(s)
        # return the values
        return result.values()


if __name__ == "__main__":
    print(Solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))