def getPriority(item):
    priority = 0
    if item.isupper():
        priority = ord(item.lower()) - 70
    else:
        priority += ord(item) - 96

    return priority


def getCommonItem(rucksack):
    half = len(rucksack) // 2
    comp1, comp2 = rucksack[:half], rucksack[half:]

    for item in comp1:
        if item in comp2:
            return getPriority(item)


def getBadges(elf1, elf2, elf3):
    badge_val = 0
    for item in elf1:
        if item in elf2 and item in elf3:
            badge_val = getPriority(item)

    return badge_val


# Read input
with open("data.txt") as f:
    rucksacks = f.read().splitlines()

# Answers for each part
part1 = 0
part2 = 0

# Loop through the rucksacks by a step of 3
for i in range(0, len(rucksacks), 3):
    # Add the priority of the common item of each compartment to part 1
    part1 += getCommonItem(rucksacks[i])
    part1 += getCommonItem(rucksacks[i + 1])
    part1 += getCommonItem(rucksacks[i + 2])

    # Add the priority of the common item in 3 rucksacks
    part2 += getBadges(rucksacks[i], rucksacks[i + 1], rucksacks[i + 2])

# Output the answers
print(part1, part2)
