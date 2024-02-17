from collections import Counter

class Solution:
    def checkInclusion(self, string1: str, string2: str) -> bool:
        # check for the length of the string1 against length of string2, if length of string1 is greater than string2 than it can not be substring of the string2
        s1Length = len(string1)
        if s1Length > len(string2): return False

        # create two variables which will store the frequency of string1 and string2's sub-string till the length of string1
        answerKey, currentWindow = Counter(string1), Counter(string2[:s1Length])

        for index, currentChar in enumerate(string2[s1Length:], start=s1Length):
            if currentWindow == answerKey: return True

            startChar = string2[index - s1Length]

            currentWindow[startChar] -= 1
            currentWindow[currentChar] += 1

            if currentWindow[startChar] == 0:
                del currentWindow[startChar]

        return currentWindow == answerKey


"""
string1: "ab"
string2: "eidbaooo"

s1Length = 2

answerKey = Counter({"a": 1, "b": 1})
currentWindow = Counter({"b": 1, "a": 1})

index = 5
currentChar = 0

startChar = string2[4-2] => string2[2] => d

currentWindow[startChar] -= 1 => currentWindow => Counter({{"d": 0, "b": 1}})
currentWindow[currentChar] += 1 => Counter({"d": 0, "b": 1, "a": 1})

del currentWindow[startChar]



"""
