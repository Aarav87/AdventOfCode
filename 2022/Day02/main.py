# Read input
with open("data.txt") as f:
    gameChoices = f.read().splitlines()

# Outcomes of each opponent move (win, draw, loss)
outcomes = {"A": [2, 1, 3], "B": [3, 2, 1], "C": [1, 3, 2]}

# Points for each shape
shapePoints = {"X": 1, "Y": 2, "Z": 3}
winResult = {"X": "C", "Y": "A", "Z": "B"}
drawResult = {"X": "A", "Y": "B", "Z": "C"}

part1 = 0
part2 = 0
for choice in gameChoices:
    oppChoice, outcome = choice.split()

    # Part 1
    if drawResult[outcome] == oppChoice:
        part1 += 3
    elif winResult[outcome] == oppChoice:
        part1 += 6
    part1 += shapePoints[outcome]

    # Part 2
    if outcome == "X":
        part2 += outcomes[oppChoice][2]
    elif outcome == "Y":
        part2 += outcomes[oppChoice][1] + 3
    else:
        part2 += outcomes[oppChoice][0] + 6

print(part1)
print(part2)
