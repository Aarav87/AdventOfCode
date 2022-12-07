# Read input
with open("data.txt") as f:
    pairs = f.read().splitlines()

# Store the answers
part1 = 0
part2 = 0

# Loop through each pair
for pair in pairs:
    # Split for each elf
    elf1, elf2 = pair.split(",")

    # Store the lower and upper value of each range
    section1 = tuple(map(int, elf1.split("-")))
    section2 = tuple(map(int, elf2.split("-")))

    # Part 1
    if section1[0] >= section2[0] and section1[1] <= section2[1]:
        part1 += 1
    elif section1[0] <= section2[0] and section1[1] >= section2[1]:
        part1 += 1

    # Part 2
    if section2[0] <= section1[0] <= section2[1]:
        part2 += 1
    elif section1[0] <= section2[0] <= section1[1]:
        part2 += 1

# Output the answers
print(part1, part2)
