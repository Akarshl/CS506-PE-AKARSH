def reverse_string(chars):
    left = 0  # start of the list
    right = len(chars) - 1  # end of the list
    

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
a = input("Enter a string: ")
char_list = list(a)
reverse_string(char_list)
print("Reversed string:", ''.join(char_list)) # Output the reversed string