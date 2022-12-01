class Solution:
    def digits_appear(self, output_values) -> int:
        # counter for how many times a 1, 4, 7, or 8 appears
        counter = 0
        # iterating through each entry in output values
        for entry in output_values:
            # iterating through each value in entry
            for value in entry:
                # increasing the counter if length of value is equal to length of segment 1, 4, 7, or 8
                if (len(value) == 2) or (len(value) == 4) or (len(value) == 3) or (len(value) == 7):
                    counter += 1

        return counter


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()

        # separate output values and put into a list
        output_values = [n.split('|')[1] for n in data]
        # remove \n and extra spaces
        output_values = [n.strip() for n in output_values]
        # separate each entry into values
        output_values = [n.split(' ') for n in output_values]

        # part 1
        Solution().digits_appear(output_values)
