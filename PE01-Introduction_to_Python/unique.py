a = int(input("Enter the number of dictionaries: "))
# Initialize an empty list to store the dictionaries
data = []
for i in range(a):
    key = input(f"Enter key for dictionary {i+1}: ")
    value = input(f"Enter value for dictionary {i+1}: ")
    data.append({key: value})
# Create a set to store unique values
unique_values = set()
for dictionary in data:
    for value in dictionary.values():
        unique_values.add(value)
print("Unique Values:", unique_values)
