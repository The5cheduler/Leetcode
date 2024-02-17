Intituation
1. check the length of the string1 and string2, if string1's length is greater than string2, string1 can not be substring of string2 so we will immidieately return False
2. Create Variable to store the length of string1
3. Create answekey and CurrentWindow Counter using Counter Class

    3.1 answerKey = Counter(string1)

    3.2 currentWindow = Counter(string2[:len(string1)])

4. Traverse through the string 2 using enumerate to access index, and value at the same time

    4.1 check if anwserKey matches with currentWindow if it does than return True

    4.2 get the startChar of the string2 by substracting current index - len(string1) => string2[index-len(string1)]

    4.3 reduce the frequency of startChar from currentWindow by 1

    4.4 Add and increase the frequency of currentChar in currentWindow by 1

    4.5 To keep the windowsize as same as length of string1, we will remove startChar if the frequency of it is 0

5. Once traversal completes it will not check the last currWindow for string2, so we will return result of answerKey == currentWindow
