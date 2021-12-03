class Solution:
    # Part 1
    def get_pos(self, commands):
        horizontal_pos = 0
        depth = 0

        for x in range(len(commands)):
            direction = commands[x].split()[0]
            amount = int(commands[x].split()[1])

            if direction == "forward":
                horizontal_pos += amount
            elif direction == "down":
                depth += amount
            else:
                depth -= amount

        print(horizontal_pos * depth)

    # Part 2
    def get_pos_aim(self, commands):
        horizontal_pos = 0
        depth = 0
        aim = 0

        for x in range(len(commands)):
            direction = commands[x].split()[0]
            amount = int(commands[x].split()[1])

            if direction == "forward":
                horizontal_pos += amount
                depth += aim * amount
            elif direction == "down":
                aim += amount
            else:
                aim -= amount

        print(horizontal_pos * depth)


# Read data from txt and add to list
with open("data.txt") as f:
    data = [line.strip() for line in f]

if __name__ == "__main__":
    Solution().get_pos(data)
    Solution().get_pos_aim(data)
