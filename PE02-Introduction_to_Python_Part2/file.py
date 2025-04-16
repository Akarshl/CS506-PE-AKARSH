def count_words_in_file(filename): # function to count the number of words in a file
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' was not found.")
        return 0

def guest_book(): # function to manage the guest book
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
  