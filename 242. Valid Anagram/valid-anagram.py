def isAnagram(s:str, t:str) -> bool:
    # compare the len of both strings
    if len(s) != len(t):
        return False

    # create hash maps to store the frequency of each character
    mapS, mapT = {}, {}

    # traverse and feed the character frequency to associated hashmaps
    for i in range(len(s)):
        mapS[s[i]] = 1 + mapS.get(s[i], 0)
        mapT[t[i]] = 1 + mapT.get(t[i], 0)

    # compare the value of both hashmap, if not same not anagram
    for key in mapS:
        if mapS[key] != mapT.get(key, 0):
            return False

    # if same return True
    return True

# *************** Method 2 ****************
    charCounter = defaultdict(int)

    # count the frequncy of the characters in string s
    for char in s:
        charCounter[char] += 1

    # Decrease the frequency from charCounter while traversing strig t
    for char in t:
        charCounter[char] -= 1

    # check of values in charCounter any character has non-zero value
    for value in charCounter.values():
        if value != 0:
            return False

    #if all values are zero than it is anagram
    return True


if __name__ == "__main__":
    print(isAnagram("anagram","nagaram"))