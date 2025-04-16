def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t) # check if sorted characters of both strings are equal
s = input("Enter the first string (s): ")
t = input("Enter the second string (t): ")
result = isAnagram(s, t) # check if t is an anagram of s
print("Output:", result)