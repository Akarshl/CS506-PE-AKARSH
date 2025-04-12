def remove_duplicates(nums):
    if not nums:
        return 0
    unique_index = 0
    # Start from second element and compare with the last unique one
    for i in range(1, len(nums)):
        if nums[i] != nums[unique_index]:
            unique_index += 1
            nums[unique_index] = nums[i]
    return unique_index + 1
a = input("Enter a sorted list of numbers (space-separated): ")
nums = list(map(int, a.strip().split())) # Convert the input string to a list of integers
new_length = remove_duplicates(nums)
print("New length after removing duplicates:", new_length)
print("Modified list with unique elements:", nums[:new_length])