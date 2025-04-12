def add_digits(num):
    if num == 0:
        return 0
    elif num % 9 == 0:
        return 9
    else:
        return num % 9
a = input("Enter a non-negative integer: ")
num = int(a)
if num < 0: # Check if input is valid
    print("Please enter a non-negative integer.")
else:
    result = add_digits(num)
    print("The final single-digit result is:", result)