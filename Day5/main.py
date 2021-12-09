class Solution:
    def create_grid(self) -> list:
        return [[0] * 1000 for i in range(1000)]

    def count(self, grid) -> int:
        overlaps = 0
        for row in grid:
            for point in row:
                # check if more than two lines overlap at the point
                if point >= 2:
                    overlaps += 1

        return overlaps

    def check_overlap(self, lines) -> int:
        # create grid
        grid = self.create_grid()

        for line in lines:
            # PART 1
            # check if x is same in line segment coordinates
            if line[0][0] == line[1][0]:
                # same x results in line being vertical
                y1 = min(line[0][1], line[1][1])
                y2 = max(line[0][1], line[1][1])
                for index in range(y1, y2+1):
                    # iterate and add 1 to every point overlapped by line segment
                    grid[line[0][0]][index] += 1
            # check if y is same in line segment coordinates
            elif line[0][1] == line[1][1]:
                # same y results in line being horizontal
                x1 = min(line[0][0], line[1][0])
                x2 = max(line[0][0], line[1][0])
                for index in range(x1, x2+1):
                    # iterate and add 1 to every point overlapped by line segment
                    grid[index][line[0][1]] += 1
            # PART 2
            else:
                # make sure x1 will always be smaller than x2
                line = [line[1], line[0]] if line[0][0] > line[1][0] else [line[0], line[1]]
                # coordinate variables
                x1, x2 = line[0][0], line[1][0]
                y1, y2 = line[0][1], line[1][1]

                for index in range(x2 - x1 + 1):
                    # index is positive if Δx is positive (always true)
                    x_delta = index if x2 > x1 else -index
                    # index is positive if Δy is positive (vice-versa)
                    y_delta = index if y2 > y1 else -index

                    grid[x1 + x_delta][y1 + y_delta] += 1

        return self.count(grid)


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()

        # remove \n from each coordinate
        lines = [n.strip() for n in data]
        # separate left coordinate set from right coordinate set
        lines = [n.split(' -> ') for n in lines]
        # separate x coordinate and y coordinate
        lines = [[(n.split(',')) for n in line] for line in lines]
        # convert coordinates into integers and store in tuple
        lines = [[tuple(int(coordinate) for coordinate in n) for n in line] for line in lines]

    Solution().check_overlap(lines)
