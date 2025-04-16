def longestCommonPrefix(strs):
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