class Solution:
    # Part 1
    def greater_than_previous(self, measurements) -> int:
        res = [int(num1) < int(num2) for num1, num2 in zip(measurements, measurements[1:])]

        return sum(res)

    # Part 2
    def three_measurement(self, measurements) -> int:
        sum_measurement = []
        for i in range(0, len(measurements)-2):
            sum_measurement.append(measurements[i] + measurements[i + 1] + measurements[i + 2])

        ans = self.greater_than_previous(sum_measurement)

        return ans


with open("data.txt") as f:
    depth_data = [int(x) for x in f.read().split()]

if __name__ == "__main__":
    Solution().greater_than_previous(depth_data)
    Solution().three_measurement(depth_data)
