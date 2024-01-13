from collections import Counter

def isAnagram(s:str, t:str) -> bool:
    return Counter(s) == Counter(t)

if __name__ == "__main__":
    print(isAnagram("anagram","nagaram"))