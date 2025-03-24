filename = "output.txt"

text_to_write = input("Enter text to write to the file: ")
with open(filename, "w") as file:
    file.write(text_to_write + "\n")
print(f"Data successfully written to {filename}.")

text_to_append = input("Enter additional text to append: ")
with open(filename, "a") as file:
    file.write(text_to_append + "\n")
print("Data successfully appended.")

print(f"\nFinal content of {filename}:")
with open(filename, "r") as file:
    print(file.read())