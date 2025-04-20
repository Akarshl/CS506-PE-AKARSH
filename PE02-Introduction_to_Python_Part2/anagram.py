def isAnagram(s: str, t: str) -> bool:
    """
    Determines whether two strings are anagrams of each other. An anagram is a word or phrase formed by rearranging the letters 
    of another, using all the original letters exactly once.
    Parameters:
    s (str): The first string.
    t (str): The second string.
    Returns:
    bool: True if t is an anagram of s, False otherwise.
    """
    return sorted(s) == sorted(t) # check if sorted characters of both strings are equal
s = input("Enter the first string (s): ")
t = input("Enter the second string (t): ")
result = isAnagram(s, t) # check if t is an anagram of s
print("Output:", result)