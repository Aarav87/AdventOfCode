class Solution:
    def __init__(self):
        # num of paths for part 1 and part 2
        self.paths = [0, 0]
        # caves visited for part 1
        self.visited_once = []
        # caves visited for part 2
        self.visited_twice = {}

    def visit_once(self, cave, connections):
        """part 1"""
        # check if cave is not end cave
        if not cave == "end":
            # return if cave is small cave and has been visited
            if cave.islower() and cave in self.visited_once:
                return
            else:
                # append caves to list of visited caves
                self.visited_once.append(cave)
                # iterate through the caves that the current cave is connected to
                for connection in connections[cave]:
                    # call recursive function with new cave
                    self.visit_once(connection, connections)

                # remove cave from visited if it is a small cave
                if cave.islower():
                    self.visited_once.remove(cave)
        else:
            # increase number of paths by 1 if it is the end cave
            self.paths[0] += 1

    def visit_twice(self, cave, connections):
        """part 2"""
        # check if cave is not end cave
        if not cave == "end":
            # check if cave is small cave
            if cave.islower():
                # increase the number of times the cave was visited
                self.visited_twice[cave] += 1

                # num of small caves that are visited more than once
                visited_more_than_once = 0

                # iterate through each cave in visited twice dictionary
                for small_cave in self.visited_twice:
                    # increase the num of caves visited more than once if the cave has been visited more than once
                    if self.visited_twice[small_cave] > 1:
                        visited_more_than_once += 1

                    # reduce the amount of times the cave was visited if the cave has been visited more than twice
                    if self.visited_twice[small_cave] > 2:
                        self.visited_twice[cave] -= 1
                        return

                # check if more than one small cave has been visited more than once
                if visited_more_than_once > 1:
                    # reduce the amount of times the cave was visited
                    self.visited_twice[cave] -= 1
                    return

            # iterate through the caves that the current cave is connected to
            for connection in connections[cave]:
                # check if the connected cave is not the start cave
                if not connection == "start":
                    # call recursive function
                    self.visit_twice(connection, connections)

            # reduce the amount of times the cave was visited if it is a small cave
            if cave.islower():
                self.visited_twice[cave] -= 1
        else:
            # increase number of paths by 1 if it is the end cave
            self.paths[1] += 1

    def find_paths(self, caves, connections) -> tuple:
        # iterate through each cave in caves
        for i, j in caves:
            # set cave to 0 in visited twice dictionary
            self.visited_twice[i] = 0
            self.visited_twice[j] = 0

        # part 1
        self.visit_once("start", connections)
        # part 2
        self.visit_twice("start", connections)

        # return answer to part 1 and part 2
        return self.paths[0], self.paths[1]


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()

        # remove \n from each entry in data
        caves = [entry.strip() for entry in data]
        # split each entry into 2 caves
        caves = [entry.split("-") for entry in caves]

        # dictionary of the caves that each cave is connected to
        connections = dict()
        # iterate through each entry in caves
        for entry in caves:
            # set each cave in connections to an empty list
            connections[entry[0]] = []
            connections[entry[1]] = []

        # iterate through each cave in caves
        for i, j in caves:
            # append the cave to the list of the cave it connects to
            connections[i].append(j)
            connections[j].append(i)

        Solution().find_paths(caves, connections)
