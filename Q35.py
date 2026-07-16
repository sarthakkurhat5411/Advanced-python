n = int(input("Enter the number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input()))

largest = max(lst)

print("Largest element:", largest)