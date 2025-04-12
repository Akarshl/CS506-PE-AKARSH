def number_of_steps(num):
    steps = 0  # Start counting from 0
    while num > 0:
        if num % 2 == 0:
            num = num // 2  
        else:
            num = num - 1   
        steps = steps + 1 
    return steps
a = input("Enter a non-negative integer: ") # Ask the user to enter a number
num = int(a)
if num < 0:
    print("Please enter a non-negative integer.")
else:
    result = number_of_steps(num)
    print("Number of steps to reduce", num, "to zero is:", result)