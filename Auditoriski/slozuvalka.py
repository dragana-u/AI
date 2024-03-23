from searching_framework.utils import Problem
from searching_framework.informed_search import *


class Slozuvalka1(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()
        index_of_empty_slot = state.index("*")

        # Up
        if index_of_empty_slot > 2:
            new_state = list(state)
            new_state[index_of_empty_slot] = new_state[index_of_empty_slot - 3]
            new_state[index_of_empty_slot - 3] = "*"
            new_state = ''.join(new_state)
            successors["Up"] = new_state
        # Down
        if index_of_empty_slot <= 5:
            new_state = list(state)
            new_state[index_of_empty_slot] = new_state[index_of_empty_slot + 3]
            new_state[index_of_empty_slot + 3] = "*"
            new_state = ''.join(new_state)
            successors["Down"] = new_state
        # Right
        if index_of_empty_slot % 3 != 2:
            new_state = list(state)
            new_state[index_of_empty_slot] = new_state[index_of_empty_slot + 1]
            new_state[index_of_empty_slot + 1] = "*"
            new_state = ''.join(new_state)
            successors["Right"] = new_state
        # Left
        if index_of_empty_slot % 3 != 0:
            new_state = list(state)
            new_state[index_of_empty_slot] = new_state[index_of_empty_slot - 1]
            new_state[index_of_empty_slot - 1] = "*"
            new_state = ''.join(new_state)
            successors["Left"] = new_state

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        counter = 0
        for x, y in zip(node.state, self.goal):
            if x != y:
                counter = counter + 1
        return counter


class Slozuvalka2(Slozuvalka1):
    coordinates = {
        0: (0, 2), 1: (1, 2), 2: (2, 2),
        3: (0, 1), 4: (1, 1), 5: (2, 1),
        6: (0, 0), 7: (1, 0), 8: (2, 0)
    }

    @staticmethod
    def mhd(n, m):
        x1, y1 = Slozuvalka2.coordinates[n]
        x2, y2 = Slozuvalka2.coordinates[m]
        return abs(x1 - x2) + abs(y1 - y2)

    def h(self, node):
        sum_value = 0
        for x in '12345678':
            val = Slozuvalka2.mhd(node.state.index(x), int(x))
            sum_value += val
        return sum_value


if __name__ == '__main__':
    slozuvalka1 = Slozuvalka1("*32415678", "*12345678")

    result1 = astar_search(slozuvalka1)
    print(result1.solve())
    result2 = greedy_best_first_graph_search(slozuvalka1)
    print(result2.solve())
    result3 = recursive_best_first_search(slozuvalka1)
    print(result3.solution())

    puzzle2 = Slozuvalka2("*32415678", "*12345678")

    result4 = astar_search(puzzle2)
    print(result4.solve())
    result5 = greedy_best_first_graph_search(puzzle2)
    print(result5.solve())
    result6 = recursive_best_first_search(puzzle2)
    print(result6.solution())
