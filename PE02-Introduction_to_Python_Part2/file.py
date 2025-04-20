def count_words_in_file(filename): # function to count the number of words in a file
    """
    Counts the number of words in the specified file.
    Parameters:
    filename (str): The name of the file to read.
    Returns:
    int: The number of words in the file.
         Returns 0 if the file is not found.
    """
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' was not found.")
        return 0

def guest_book(): # function to manage the guest book
    """
    Manages a simple guest book. Continuously prompts users to enter their names and appends each name to a file named 'guest_book.txt'. Users can type 'q' to quit """
    print("\nGuest Book")
    print("Enter 'q' to quit.")
    while True:
        name = input("Enter your name: ")
        if name.lower() == 'q':
            print("Exiting guest book...\n")
            break
        print(f"Hello, {name}! Nice to meet you.")
        with open("guest_book.txt", "a") as file:
            file.write(f"{name} visited the site.\n")

def read_file(filename): # function to read and print the contents of a file
    """
    Reads and displays the contents of the specified file.
    Parameters:
    filename (str): The name of the file to read.
    Returns:
    None
    """
    try:
        with open(filename, 'r') as file:
            print(f"\nContents of {filename}:")
            print(file.read())
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")

if __name__ == "__main__":
    print("Word Counter")
    filename = input("Enter the filename to count words from: ")
    count = count_words_in_file(filename)
    print(f"Number of words in '{filename}': {count}")
    guest_book()
    print("\nReading Files")
    read_file("sample.txt")
  