file = open("sample.txt", "w")
data = input("Enter text: ")
file.write(data)
file.close()

print("Data written successfully.")