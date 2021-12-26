class Solution:
    @staticmethod
    def create_grid(max_x, max_y):
        # create grid using largest x and y value
        return [["."] * (max_x + 1) for i in range(max_y + 1)]

    @staticmethod
    def count_dots(grid) -> int:
        """part 1"""

        # num of dots
        dots = 0
        # iterate through y in grid
        for y in range(len(grid)):
            # iterate through x in grid
            for x in range(len(grid[y])):
                # add 1 to num of dots if value is a dot
                if grid[y][x] == "#":
                    dots += 1

        return dots

    @staticmethod
    def get_letter_code(grid):
        """part 2"""

        # print every row in grid to get letter code
        for row in grid:
            print(row)

    @staticmethod
    def foldX(grid, x_fold):
        # point where grid folds over x
        x_fold = int(x_fold.split("=")[1])
        # iterate through y in grid
        for y in range(len(grid)):
            # iterate from the point where grid folds over x to the end of the list
            for x in range(x_fold + 1, len(grid[y])):
                # check if value is a dot
                if grid[y][x] == "#":
                    # new x is the difference between length of y in grid and old x
                    new_x = (len(grid[y]) - 1) - x
                    # set new x to a dot
                    grid[y][new_x] = "#"

        # update grid to not include points that were folded
        grid[:] = [[grid[y][x] for x in range(x_fold)] for y in range(len(grid))]

    @staticmethod
    def foldY(grid, y_fold):
        # point where grid folds over y
        y_fold = int(y_fold.split("=")[1])
        # iterate from the point where grid folds over y to the end of the list
        for y in range(y_fold + 1, len(grid)):
            # iterate through x in grid
            for x in range(len(grid[y])):
                # check if value is a dot
                if grid[y][x] == "#":
                    # new y is the difference between length of grid and old y
                    new_y = (len(grid) - 1) - y
                    # set new y to a dot
                    grid[new_y][x] = "#"

        # update grid to not include points that were folded
        grid[:] = [grid[y] for y in range(y_fold)]

    def fold(self, grid, folds):
        # num of folds
        num_of_folds = 0
        # iterate through each fold instruction
        for fold in folds:
            # increase num of folds
            num_of_folds += 1

            # call foldX if instruction folds along x
            if fold.startswith('x'):
                self.foldX(grid, fold)
            else:
                # call foldY if instruction folds along y
                self.foldY(grid, fold)

            # call count dots function if num of folds is equal to 1
            if num_of_folds == 1:
                self.count_dots(grid)

        self.get_letter_code(grid)

    def add_dots(self, coordinates, fold, max_x, max_y):
        # create grid
        grid = self.create_grid(max_x, max_y)

        # iterate through each coordinate in coordinates
        for coordinate in coordinates:
            # set x and y value
            x, y = coordinate[0], coordinate[1]
            # set coordinate in grid to a dot
            grid[y][x] = "#"

        # call fold function
        self.fold(grid, fold)


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()

        # remove \n from each line in data
        data = [line.strip() for line in data]
        # split each line into x, y
        data = [line.split(',') for line in data]

        """organise data into coordinates and folding instructions"""
        # list of coordinates for dots
        coordinates = []
        # list of folding instructions
        fold = []

        # largest x and y coordinate
        max_x, max_y = 0, 0

        # iterate through each line in data
        for line in data:
            # append (x, y) to list of coordinates if length of line is greater than 2
            if len(line) >= 2:
                x, y = int(line[0]), int(line[1])
                max_x = int(x) if int(x) > max_x else max_x
                max_y = int(y) if int(y) > max_y else max_y
                coordinates.append((x, y))
            else:
                # append to fold instructions if line is not empty
                if line[0]:
                    fold.append(line[0].split('fold along')[1].strip())

        Solution().add_dots(coordinates, fold, max_x, max_y)
