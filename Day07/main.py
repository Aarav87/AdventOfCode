class Solution:
    def fuel_cost1(self, fuels, costs) -> int:
        # iterate through each cost in dict
        for cost in range(len(costs)+1):
            # set the cost of moving ships to that index
            costs[cost] = sum([abs(fuel-cost) for fuel in fuels])

        return min(costs.values())

    def fuel_cost2(self, fuels, costs) -> int:
        # iterate through each cost in dict
        for cost in range(len(costs)+1):
            # set the cost of moving ships to that index
            costs[cost] = sum([abs(fuel-cost)*(abs(fuel-cost)+1)//2 for fuel in fuels])

        return min(costs.values())


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readline()

        # put data into list and remove commas
        data = data.split(",")
        # convert every element in list into integer
        data = [int(x) for x in data]
        # dict that holds the cost of moving crab submarines to every index
        costs = {x: 0 for x in range(len(data))}

        # part 1
        Solution().fuel_cost1(data, costs)
        # part 2
        Solution().fuel_cost2(data, costs)
