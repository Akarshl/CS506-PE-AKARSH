def longestCommonPrefix(strs):
    """
    Finds the longest common prefix string amongst a list of strings.

    The function compares characters from the beginning of the first string 
    with each subsequent string in the list. If a mismatch is found, the prefix 
    is shortened until a match is found or no common prefix exists.
    Parameters:
    strs (List[str]): A list of strings to evaluate.
    Returns:
    str: The longest common prefix shared among all strings in the list.
         Returns an empty string if there is no common prefix.
    """
    if not strs:
        return ""
    prefix = strs[0] # assuming the first string is the common prefix
    for word in strs[1:]: # Compare it with each string in the list
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix
user_input = input("Enter strings separated by space: ")
strs = user_input.split()
result = longestCommonPrefix(strs)
print("Longest common prefix:", '"' + result + '"')