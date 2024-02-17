# Intituation

## Algorithm 1:

### 1. Length Check:
- If the lengths of the two strings are not equal, they cannot be anagrams. Return False immediately.

### 2. Frequency Counting:
- Create an empty HashMap (or any similar data structure) to store character frequencies for each string.
- Iterate through the first string:
  - For each character, increment its count in the HashMap. If the character isn't found, add it to the HashMap with a count of 1.

### 3. Comparison:

- Iterate through HashMap create for first string
    - Repeat the same process for the second string, decrementing counts instead of incrementing
    - if character not found in hashMap than return `False` as both strings as different characters
- If all entries in the first HashMap have matching entries in the second HashMap, the strings are anagrams. Return True.




## Algorithm 2:

### 1. Length Check:
- If the lengths of the two strings are not equal, they cannot be anagrams. Return False immediately.

### 2. Frequency Counting:
- Create an empty HashMap (or any similar data structure) to store character frequencies for each string.
- Iterate through the first string:
  - For each character, increment its count in the HashMap. If the character isn't found, add it to the HashMap with a count of 1. Perform this step for both strings.

### 3. Comparison:
- Iterate through the first HashMap:
  - For each character and its count:
    - If the same character is not found in the second HashMap with the same count, the strings are not anagrams. Return False.
- If all entries in the first HashMap have matching entries in the second HashMap, the strings are anagrams. Return True.

