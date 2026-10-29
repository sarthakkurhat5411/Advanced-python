with open("input.txt", "r") as file:
    data = file.read()

data = data.upper()

with open("output.txt", "w") as file:
    file.write(data)

print("File content converted to uppercase successfully")

