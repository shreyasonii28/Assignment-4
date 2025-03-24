filename = "sample.txt"

try:
    with open(filename, "r") as file:
        reading_file = file.read()
        print("Reading file content:\n")
        print(reading_file)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")