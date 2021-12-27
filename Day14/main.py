from collections import defaultdict


class Solution:
    def pair_insertion(self, frequency, template, rules, steps) -> int:
        # list of the result of pair frequency dict after each step
        res = [frequency]
        # iterate through each step
        for _ in range(steps):
            # set frequency to the latest pair frequency dict in res
            frequency = res[-1]
            # set pair freq to frequency
            pair_freq = frequency.copy()

            # iterate through each pair in frequency
            for pair in frequency:
                # iterate through each rule in insertion rules
                for rule in rules:
                    # check if insertion string is equal to pair
                    if rule[0] == pair:
                        # increase the frequency of the new pairs that were formed during the pair insertion
                        pair_freq[pair[0] + rule[1]] += frequency[pair]
                        pair_freq[rule[1] + pair[1]] += frequency[pair]
                        # reset the value of the original pair in pair freq
                        pair_freq[pair] -= frequency[pair]
            # append pair freq to res after the step
            res.append(pair_freq)

        # calculate polymer score
        return self.polymer_score(template, res[-1])

    @staticmethod
    def polymer_score(template, pair_freq) -> int:
        # dict of number of times each element appears
        elements = defaultdict(int)
        # iterate through each pair in pair frequency
        for pair in pair_freq:
            # add 1 to the value of that element in the elements dict
            elements[pair[0]] += pair_freq[pair]
            elements[pair[1]] += pair_freq[pair]

        # add 1 to the value of the last element in template
        elements[template[-1]] += 1
        # divide each value by 2 because they are counted twice
        element_values = [val // 2 for val in elements.values()]

        return max(element_values) - min(element_values)


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()

        # remove \n from each line
        data = [line.strip() for line in data]
        # polymer template
        polymer_template = data[0]
        # pair insertion rules
        insertion_rules = [data[line].split('->') for line in range(2, len(data))]
        # remove extra spaces from each insertion rule
        insertion_rules = [[string.strip() for string in line] for line in insertion_rules]

        # dict of number of times each pair appears
        pair_frequency = defaultdict(int)
        # iterate through every pair in polymer template
        for i in range(len(polymer_template)-1):
            # add 1 to the value of that pair in the pair frequency dict
            pair_frequency[polymer_template[i:i+2]] += 1

        # part 1
        Solution().pair_insertion(pair_frequency, polymer_template, insertion_rules, steps=10)
        # part 2
        Solution().pair_insertion(pair_frequency, polymer_template, insertion_rules, steps=40)
