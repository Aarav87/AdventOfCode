# Read input
with open("data.txt") as f:
    calories = f.read().splitlines()

# List of all the elfs' total calories
elfs = []
curr = 0

# Loop through each calorie
for cal in calories:
    # Add the calories to curr if it is the same elf
    if cal != "":
        curr += int(cal)
    else:
        # Append curr to list elfs and reset curr
        elfs.append(curr)
        curr = 0

elfs.sort()

# Part 1
print(elfs[-1])

# Part 2
print(sum(elfs[-3:]))
