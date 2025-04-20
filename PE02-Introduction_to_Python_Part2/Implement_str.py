def strStr(haystack: str, needle: str) -> int:
    """
    Finds the index of the first occurrence of the substring 'needle' in the string 'haystack'.
    Parameters:
    haystack (str): The main string to search within. needle (str): The substring to search for.
    Returns:
    int: The index of the first occurrence of 'needle' in 'haystack'. Returns 0 if 'needle' is an empty string. Returns -1 if 'needle' is not found in 'haystack' """
    if needle == "": # If needle is an empty string return 0
        return 0
    for i in range(len(haystack) - len(needle) + 1): #find the first occurrence of needle
        if haystack[i:i+len(needle)] == needle: # compare substring with needle
            return i
    return -1
haystack = input("Enter the haystack string: ")
needle = input("Enter the needle string: ")
result = strStr(haystack, needle)
print("Output:", result)