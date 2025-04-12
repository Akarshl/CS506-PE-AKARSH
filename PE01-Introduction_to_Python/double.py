def check_if_exist(arr):
    seen = set()  # To store elements
    for num in arr:
        if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
            return True
        seen.add(num)
    return False
a = input("Enter a list of integers (space-separated): ")
# Convert input to a list of integers
arr = list(map(int, a.strip().split()))
result = check_if_exist(arr)
print("Output:", result)