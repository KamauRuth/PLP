# File Creation
with open("my_file.txt", "w") as file:
    file.write("This is line 1\n")
    file.write("12345\n")
    file.write("Python File Handling\n")

# File Reading and Display
with open("my_file.txt", "r") as file:
    content = file.read()
    print("File Contents:")
    print(content)

# File Appending
with open("my_file.txt", "a") as file:
    file.write("Additional line 1\n")
    file.write("67890\n")
    file.write("Appending to an existing file\n")

# Error Handling
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("Error handling completed.")

