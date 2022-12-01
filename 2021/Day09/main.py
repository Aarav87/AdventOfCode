class Solution:
    def __init__(self):
        # list of all low point coordinates in heightmap
        self.low_points = []
        # list of all basins in heightmap
        self.basins = []
        # sum of the risk levels of all low points
        self.risk_level = 0
        # product of the sizes of three largest basins
        self.product = 1

    def risk_level_sum(self) -> int:
        return self.risk_level

    def basin_product(self) -> int:
        # sort basins by length to get the three largest basins
        largest_basins = sorted(self.basins, key=len)[-3:]
        # iterate through each basin in the largest basins
        for basin in largest_basins:
            # multiply the product by the length of the basin
            self.product *= len(basin)

        return self.product

    def get_low_points(self, heightmap):
        # iterate through each row in heightmap
        for x in range(len(heightmap)):
            # iterate through each column in heightmap
            for y in range(len(heightmap[0])):
                # list of neighbours of value
                neighbours = []

                # check if x-1 is in range
                if x-1 >= 0:
                    # append to neighbours
                    neighbours.append(heightmap[x-1][y])
                # check if x+1 is in range
                if x+1 < len(heightmap):
                    # append to neighbours
                    neighbours.append(heightmap[x+1][y])
                # check if y-1 is in range
                if y-1 >= 0:
                    # append to neighbours
                    neighbours.append(heightmap[x][y-1])
                # check if y+1 is in range
                if y+1 < len(heightmap[0]):
                    # append to neighbours
                    neighbours.append(heightmap[x][y+1])

                # check for low point if value is smaller than its smallest neighbour
                if heightmap[x][y] < min(neighbours):
                    # add to the risk level
                    self.risk_level += (1 + heightmap[x][y])
                    # add coordinate to low points list
                    self.low_points.append((x, y))

        # iterate through each coordinate set in low points
        for coordinate in range(len(self.low_points)):
            # add empty list to list of basins
            self.basins.append([])
            # call find basins function
            self.find_basins(heightmap, coordinate, self.low_points[coordinate][0], self.low_points[coordinate][1])

        # part 1
        self.risk_level_sum()
        # part 2
        self.basin_product()

    def find_basins(self, heightmap, basin, x, y):
        """recursion for part 2"""
        # check if value is a 9
        if not heightmap[x][y] == 9:
            # add value to list of basins
            self.basins[basin].append(heightmap[x][y])

            # check if x-1 is in range
            if x-1 >= 0:
                # check if neighbour is larger than current value
                if heightmap[x-1][y] > heightmap[x][y]:
                    # call recursive function with updated parameters
                    self.find_basins(heightmap, basin, x-1, y)
            # check if x+1 is in range
            if x+1 < len(heightmap):
                # check if neighbour is larger than current value
                if heightmap[x+1][y] > heightmap[x][y]:
                    # call recursive function with updated parameters
                    self.find_basins(heightmap, basin, x+1, y)
            # check if y-1 is in range
            if y-1 >= 0:
                # check if neighbour is larger than current value
                if heightmap[x][y-1] > heightmap[x][y]:
                    # call recursive function with updated parameters
                    self.find_basins(heightmap, basin, x, y-1)
            # check if y+1 is in range
            if y+1 < len(heightmap[0]):
                # check if neighbour is larger than current value
                if heightmap[x][y+1] > heightmap[x][y]:
                    # call recursive function with updated parameters
                    self.find_basins(heightmap, basin, x, y+1)

            # set value to 9 so it is not used again
            heightmap[x][y] = 9


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()

        # remove \n from each row
        heightmap = [row.strip() for row in data]
        # convert each number into integer
        heightmap = [[int(num) for num in row] for row in heightmap]

        Solution().get_low_points(heightmap)
