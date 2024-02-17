class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # check if t is valid and length of t is smaller than length of s, it not return empty string
        if not t or len(t) > len(s):
            return ""

        # define two hashmap to store the frequency of each characters in string t and string s's window
        countT, countWindow = {}, {}

        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        # initialize the result and result length
        result, resultLength = [-1,-1], float("infinity")
        leftPointer = 0

        # initialize to variables have and need to check if condition is met or not
        have, need = 0, len(countT)

        # traverse the string s while keept rightPointer at left most position
        for rightPointer in range(len(s)):
            # get the character value at rightpointer for strings
            currentChar = s[rightPointer]
            # update the countWindow hashMap with new frequency for currentChar
            countWindow[currentChar] = 1 + countWindow.get(currentChar, 0)

            # if currentChar is in countT and frequency value is same in countWindow and countT hashMaps than increment have value with 1
            if currentChar in countT and countWindow[currentChar] == countT[currentChar]:
                have += 1

            # if value of have is same as need
            while have == need:
                # check if current length between rightPointer and leftPointer is less than current resultLength
                if (rightPointer - leftPointer + 1) < resultLength:
                    result = [leftPointer, rightPointer]
                    resultLength = (rightPointer - leftPointer + 1)

                # while have is same as need decrement the frequency of left most character
                countWindow[s[leftPointer]] -= 1

                # check if decrementing leftPointer's frequency
                if s[leftPointer] in countT and countWindow[s[leftPointer]] < countT[s[leftPointer]]:
                    have -= 1

                leftPointer += 1 # move the leftPointer to shrink the window

        leftPointer, rightPointer = result # assign value of result to leftPointer and rightPointer
        # Return the minimum window if found, otherwise return an empty string:
        return s[leftPointer : rightPointer + 1] if result != float("infinity") else ""






