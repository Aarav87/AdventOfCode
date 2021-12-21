class Solution:
    def __init__(self):
        # left characters
        self.left = "([{<"
        # right characters
        self.right = ")]}>"

    def error_score(self, corrupted) -> int:
        # syntax error score table
        score_table = [3, 57, 1197, 25137]
        # total syntax error score
        score = 0

        # iterate through each corrupted character
        for char in corrupted:
            # add to score using score table
            score += score_table[self.right.find(char)]

        return score

    def middle_score(self, incomplete) -> int:
        # incomplete character score table
        score_table = [1, 2, 3, 4]
        # score for each incomplete line
        scores = []

        # iterate through each incomplete line
        for line in incomplete:
            # set score to 0
            score = 0
            # iterate through each character in line backwards
            for char in line[::-1]:
                # multiply the score by 5 and add the corresponding completion string score
                score = (score * 5) + score_table[self.left.find(char)]
            # append score to list of scores
            scores.append(score)

        # return middle score
        return sorted(scores)[len(scores) // 2]

    def scores(self, chunks):
        # list of corrupted and incomplete lines
        corrupted, incomplete = [], []
        # list of corrupt characters
        corrupt_chars = []

        # iterate through each line in chunks
        for line in chunks:
            # set corrupt to False
            corrupt = False
            # list of incomplete characters
            incomplete_chars = []

            # iterate through each character in line
            for char in line:
                # check if character is in left characters
                if char in self.left:
                    # append to corrupt chars and incomplete chars
                    corrupt_chars.append(char)
                    incomplete_chars.append(char)
                # check if character is in right characters
                elif char in self.right:
                    # check if last character is not equal to character in left
                    if corrupt_chars[-1] != self.left[self.right.find(char)]:
                        # append to corrupted
                        corrupted.append(self.right[self.right.find(char)])
                        # set corrupt to True
                        corrupt = True
                        break
                    else:
                        # remove from corrupt chars and incomplete chars if character
                        corrupt_chars.pop()
                        incomplete_chars.pop()
            # check if corrupt is False
            if not corrupt:
                # append incomplete characters to list
                incomplete.append("".join(incomplete_chars))

        # part 1
        self.error_score(corrupted)
        # part 2
        self.middle_score(incomplete)


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()

        # remove \n from each row
        chunks = [row.strip() for row in data]

        Solution().scores(chunks)
