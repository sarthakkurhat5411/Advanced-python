def count_lines(filename):
    with open(filename, "r") as f:
        return sum(1 for line in f)


def extract_first_two_lines(filename):
    with open(filename, "r") as f:
        lines = []
        for i, line in enumerate(f):
            if i == 2:
                break
            lines.append(line)
        return lines


def write_lines(filename, lines):
    with open(filename, "w") as f:
        f.writelines(lines)


# Main program
input_file = "input.txt"
output_file = "output.txt"

total_lines = count_lines(input_file)
print("Total number of lines:", total_lines)

first_two = extract_first_two_lines(input_file)

write_lines(output_file, first_two)

print("First two lines written successfully.")
# input text in other file 
# where i had input (Apple, Banana, Mango, Orange, Grapes) and then 