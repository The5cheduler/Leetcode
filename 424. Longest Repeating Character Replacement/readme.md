# Approach 1 => $$O(26*n)$$
1. create the Hashmap to store the frequency of each character in the string
2. create variable named, result, leftPointer
3. Traverse through the string and update the count with character and frequency
4. calculate the current window (rightPointer - leftPointer + 1)
5. if or while currentWindow - maximum frequency in count is greater the replacement k  than

    5.1 Decrease the frequency of character at leftPointer in string by 1
    5.1 Increment the leftPointer untill  condition becomes false
    5.1 recalculate the currentWindow
6. update the result by checking maximum of current result with currentWindows
7. Once successful traversal return result with maximum length with character replacement

# Approach 2 --> $$O(n)$$
1. create the Hashmap to store the frequency of each character in the string
2. create variable named, result, leftPointer, and MaxFrequency
3. Traverse through the string and update the count with character and frequency
4. update maxFrequency by checking max of current maxFrequency with frequency of latest update characterFrequency at s[rightPointer]
5. calculate the current window (rightPointer - leftPointer + 1)
6. if or while currentWindow - maxFrequency is greater the replacement k  than

    6.1 Decrease the frequency of character at leftPointer in string by 1
    6.1 Increment the leftPointer untill  condition becomes false
    6.1 recalculate the currentWindow
7. update the result by checking maximum of current result with currentWindows
8. Once successful traversal return result with maximum length with character replacement
