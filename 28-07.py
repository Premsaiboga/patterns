# Create or overwrite the file
with open("data.txt", "w") as file:
    file.write("Hello\n")
    file.write("Welcome to file handling!\n")

# Read the file content
with open("data.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)

# Add new content to existing file
with open("data.txt", "a") as file:
    file.write("This is an appended line.\n")

#Delete file
import os

if os.path.exists("data.txt"):
    os.remove("data.txt")
    print("File deleted.")
else:
    print("File does not exist.")
