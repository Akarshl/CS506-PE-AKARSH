def strStr(haystack: str, needle: str) -> int:
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