def isAnagram(str1, str2):
    # Check if the lengths of the two strings are different, if so, they cannot be anagrams
    if len(str1) != len(str2):
        return False
    
    # Initialize dictionaries to store character counts for each string
    mapS1, mapS2 = {}, {}
    
    # Populate dictionaries with character counts for each string
    for i in range(len(str1)):
        mapS1[str1[i]] = 1 + mapS1.get(str1[i], 0)
        mapS2[str2[i]] = 1 + mapS2.get(str2[i], 0)

    # Compare the character counts in both dictionaries
    for key in mapS1:
        # If counts are different, the strings are not anagrams
        if mapS1[key] != mapS2.get(key, 0):
            return False

    # If all character counts match, the strings are anagrams
    return True
