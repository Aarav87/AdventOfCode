class Solution:
    # Part 1
    def greater_than_previous(self, measurements):
        res = [int(sub1) < int(sub2) for sub1, sub2 in zip(measurements, measurements[1:])]

        print(sum(res))

    # Part 2
    def three_measurement(self, measurements):
        ans = []
        for i in range(0, len(measurements)-2):
            ans.append(measurements[i] + measurements[i + 1] + measurements[i + 2])

        self.greater_than_previous(ans)


with open("data.txt") as f:
    depth_data = [int(x) for x in f.read().split()]

if __name__ == "__main__":
    Solution().greater_than_previous(depth_data)
    Solution().three_measurement(depth_data)
