class Solution:
    def power_consumption(self, binary_nums) -> int:
        one_counter, zero_counter = 0, 0
        gamma_bits, epsilon_bits = [], []
        for i in range(0, 12):
            for j in range(len(binary_nums)):
                if binary_nums[j][i] == "1":
                    one_counter += 1
                else:
                    zero_counter += 1

            if one_counter > zero_counter:
                gamma_bits.append("1")
                epsilon_bits.append("0")
            else:
                gamma_bits.append("0")
                epsilon_bits.append("1")

            one_counter = 0
            zero_counter = 0

        gamma_rate = int(''.join(gamma_bits), 2)
        epsilon_rate = int(''.join(epsilon_bits), 2)

        return gamma_rate * epsilon_rate


with open("data.txt") as f:
    data = [line.strip() for line in f]

sample_data = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010",
               "01010"]

if __name__ == "__main__":
    Solution().power_consumption(data)
