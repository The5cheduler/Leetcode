class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # store the results in the defualt dictionary to handle single value list
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26 # for a .. z
            for c in s:
                # create count list with number
                count[ord(c) - ord("a")] += 1
            # map it back to results dictionary with string (it will be stored as list as we have defined default value to be list)
            result[tuple(count)].append(s)
        # return the values 
        return result.values()
