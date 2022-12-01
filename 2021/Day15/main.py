from collections import defaultdict
import heapq


class Solution:
    def find_path(self, risk_levels) -> int:
        # dict of the risk to get to each coordinate
        costs = defaultdict(int)
        # list of coordinates visited
        visited = []
        # list of cost, row, col
        pq = [(0, 0, 0)]
        # create heap queue of pq list
        heapq.heapify(pq)

        while len(pq) > 0:
            # get smallest item from heap queue
            risk, row, col = heapq.heappop(pq)

            # check if coordinate has already been visited
            if (row, col) not in visited:
                # append coordinate to visited list
                visited.append((row, col))
                # set costs of the coordinate to risk
                costs[(row, col)] = risk

                # break if endpoint has been reached
                if row == len(risk_levels) - 1 and col == len(risk_levels[0]) - 1:
                    break

                # iterate through each neighbour
                for neighbour in self.check_neighbours(row, col):
                    # row and col of neighbour
                    new_row = neighbour[0]
                    new_col = neighbour[1]
                    # push the item into the heap
                    heapq.heappush(pq, (risk + risk_levels[new_row][new_col], new_row, new_col))

        # return lowest total risk
        return costs[(len(risk_levels)-1, len(risk_levels[0])-1)]

    @staticmethod
    def check_neighbours(row, col) -> list:
        # list of coordinates of neighbours
        neighbours = []

        # append coordinate to neighbours if row-1 is in range
        if row - 1 >= 0:
            neighbours.append((row - 1, col))
        # append coordinate to neighbours if row+1 is in range
        if row + 1 < len(risk_levels):
            neighbours.append((row + 1, col))
        # append coordinate to neighbours if col-1 is in range
        if col - 1 >= 0:
            neighbours.append((row, col - 1))
        # append coordinate to neighbours if row+1 is in range
        if col + 1 < len(risk_levels[0]):
            neighbours.append((row, col + 1))

        return neighbours


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()

        # remove \n from each row
        data = [row.strip() for row in data]
        # 2d list of risk levels
        risk_levels = [[int(col) for col in row] for row in data]

        # part 1
        Solution().find_path(risk_levels)
