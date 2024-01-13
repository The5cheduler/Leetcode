def isAnagram(s:str, t:str) -> bool:
    return sorted(s) == sorted(t)

if __name__ == "__main__":
    print(isAnagram("anagram","nagarmm"))