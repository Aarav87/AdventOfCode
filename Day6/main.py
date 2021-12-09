class Solution:
    def num_of_fish(self, fishes) -> int:
        return sum(fishes.values())

    def internal_timer(self, fishes, days) -> int:
        for day in range(days):
            # store number of zeros
            num_of_zeros = fishes[0]
            # reset the number of zeros to 0
            fishes[0] = 0

            for internal_timer in range(1, len(fishes)):
                # set previous internal timer to number of current internal timer
                fishes[internal_timer-1] = fishes[internal_timer]
                # set current internal timer to 0
                fishes[internal_timer] = 0

            # add number of zeros to the six internal timer (internal timer resets every six days)
            fishes[6] += num_of_zeros
            # add number of zeros to the eight internal timer (a new fish is created for every zero)
            fishes[8] += num_of_zeros

        return self.num_of_fish(fishes)


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readline()

        # put data into list and remove commas
        data = data.split(',')
        # convert every element in list into integer
        data = [int(x) for x in data]

        lanternfish = {index: 0 for index in range(9)}
        for internal_timer in data:
            lanternfish[internal_timer] += 1

    # part 1
    Solution().internal_timer(lanternfish, days=80)
    # part 2
    Solution().internal_timer(lanternfish, days=256)
