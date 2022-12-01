class Solution:
    def __init__(self):
        # number of flashes
        self.flashes = 0
        # coordinates of each energy level flashed
        self.flashed = []

    def get_neighbours(self, x, y) -> list:
        """get adjacent neighbours"""
        # list of coordinates of neighbours
        neighbours = []

        """horizontal and vertical neighbours"""
        # append coordinate if x-1 is in range
        if x-1 >= 0:
            neighbours.append((x-1, y))
        # append coordinate if x+1 is in range
        if x+1 < len(octopuses):
            neighbours.append((x+1, y))
        # append coordinate if y-1 is in range
        if y-1 >= 0:
            neighbours.append((x, y-1))
        # append coordinate if y+1 is in range
        if y+1 < len(octopuses[0]):
            neighbours.append((x, y+1))

        """diagonal neighbours"""
        # append coordinate if x-1 and y-1 is in range
        if (x-1 >= 0) and (y-1 >= 0):
            neighbours.append((x-1, y-1))
        # append coordinate if x-1 and y+1 is in range
        if (x-1 >= 0) and (y+1 < len(octopuses[0])):
            neighbours.append((x-1, y+1))
        # append coordinate if x+1 and y-1 is in range
        if (x+1 < len(octopuses)) and (y - 1 >= 0):
            neighbours.append((x+1, y-1))
        # append coordinate if x+1 and y+1 is in range
        if (x+1 < len(octopuses)) and (y+1 < len(octopuses[0])):
            neighbours.append((x+1, y+1))

        return neighbours

    def energy_level(self, octopuses, x, y):
        # check if coordinate has not been flashed already
        if (x, y) not in self.flashed:
            # check if energy level of octopus is equal to 9 (octopus is going to flash)
            if octopuses[x][y] == 9:
                # set energy level to 0
                octopuses[x][y] = 0
                # increase flashes and append coordinate to flashed
                self.flashes += 1
                self.flashed.append((x, y))
                # iterate through each coordinate in neighbours
                for coordinate in self.get_neighbours(x, y):
                    # call recursive function with updated parameters
                    self.energy_level(octopuses, coordinate[0], coordinate[1])
            else:
                # increase energy level if it is not equal to 9
                octopuses[x][y] += 1

    def check_flashes(self, octopuses) -> list:
        # number of steps
        steps = 0
        # answer to part 1 and part 2
        ans = []

        while True:
            # increase number of steps by 1
            steps += 1
            # clear list of coordinates of each energy level flashed
            self.flashed.clear()
            # iterate through each row in octopus
            for x in range(len(octopuses)):
                # iterate through each column in octopus
                for y in range(len(octopuses[0])):
                    self.energy_level(octopuses, x, y)

            """part 1"""
            # append flashes to ans after 100 steps
            if steps == 100:
                ans.append(self.flashes)
            """part 2"""
            # append number of steps to ans when all octopuses flash simultaneously
            if len(self.flashed) == 100:
                ans.append(steps)
                break

        return ans


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()

        # remove \n from each row of data
        octopuses = [row.strip() for row in data]
        # convert each number in row into integer
        octopuses = [[int(num) for num in row] for row in octopuses]

        Solution().check_flashes(octopuses)
