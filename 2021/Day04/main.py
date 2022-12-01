class Solution:
    # Score calculator
    def final_score(self, num, board) -> int:
        score = 0
        for row in board:
            for item in row:
                if item != 'X':
                    score += int(item)

        return score * int(num)

    # PART 1
    def first_bingo(self, nums, boards):
        bingo = ['X', 'X', 'X', 'X', 'X']
        first_winner = None

        for num in nums:
            if not first_winner:
                for brd in range(len(boards)):
                    # Check for bingo in rows
                    for row in range(5):
                        for item in range(5):
                            if boards[brd][row][item] == num:
                                boards[brd][row][item] = "X"

                        if boards[brd][row] == bingo:
                            first_winner = [num, boards[brd]]

                    # Check for bingo in columns
                    for column in range(5):
                        col_list = []
                        for item in range(5):
                            col_list.append(boards[brd][item][column])
                        # Check if column is ['X','X','X','X','X']
                        if col_list == bingo:
                            first_winner = [num, boards[brd]]

        self.final_score(first_winner[0], first_winner[1])

    # PART 2
    def last_bingo(self, nums, boards):
        bingo = ['X', 'X', 'X', 'X', 'X']
        boards_left = [x for x in range(len(boards))]
        final_winner = None

        for num in nums:
            if len(boards_left) != 0:
                for brd in range(len(boards)):
                    # Check for bingo in rows
                    for row in range(5):
                        for item in range(5):
                            if boards[brd][row][item] == num:
                                boards[brd][row][item] = "X"

                        if boards[brd][row] == bingo:
                            if brd in boards_left:
                                # Remove index of bingo cards won
                                boards_left.remove(brd)
                            # Check if bingo card is last winner
                            if len(boards_left) == 1:
                                final_winner = [num, boards[boards_left[0]]]

                    # Check for bingo in columns
                    for column in range(5):
                        col_list = []
                        for item in range(5):
                            col_list.append(boards[brd][item][column])
                        if col_list == bingo:
                            if brd in boards_left:
                                # Remove index of bingo cards won
                                boards_left.remove(brd)
                            # Check if bingo card is last winner
                            if len(boards_left) == 1:
                                final_winner = [num, boards[boards_left[0]]]

        self.final_score(final_winner[0], final_winner[1])


with open("data.txt") as f:
    file = f.readlines()
    bingo_nums = file[0].strip("\n").split(",")
    bingo_boards = []

    board = []
    for line in range(2, len(file)):
        line = file[line].strip()
        # Check if line is empty
        if line:
            board.append(line.split())
        else:
            # Add board to bing boards
            bingo_boards.append(board)
            # Clear list for next board
            board = []

    # Add last board to bingo boards
    bingo_boards.append(board)

if __name__ == "__main__":
    Solution().first_bingo(bingo_nums, bingo_boards)
    Solution().last_bingo(bingo_nums, bingo_boards)
