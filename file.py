try:

    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
        print("File content:", content)
except FileNotFoundError:
    print("Error: File not found.")
