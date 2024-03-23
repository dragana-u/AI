from searching_framework.utils import Problem
from searching_framework.informed_search import *


class Istrazuvac(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()
        x_man = state[0]
        y_man = state[1]
        obstacle_1 = state[2]
        obstacle_2 = state[3]

        # Up
        new_x = x_man
        new_y = y_man + 1
        obstacle_1 = self.move_obstacle(obstacle_1)
        obstacle_2 = self.move_obstacle(obstacle_2)
        if self.check_valid(new_x, new_y, obstacle_1,
                            obstacle_2) and new_y != y_man:
            successors["Up"] = (new_x, new_y, obstacle_1, obstacle_2)

        # Down
        new_x = x_man
        new_y = y_man - 1
        obstacle_1 = self.move_obstacle(obstacle_1)
        obstacle_2 = self.move_obstacle(obstacle_2)
        if self.check_valid(new_x, new_y, obstacle_1,
                            obstacle_2) and new_y != y_man:
            successors["Down"] = (new_x, new_y, obstacle_1, obstacle_2)

        # Right
        new_x = x_man + 1
        new_y = y_man
        obstacle_1 = self.move_obstacle(obstacle_1)
        obstacle_2 = self.move_obstacle(obstacle_2)
        if self.check_valid(new_x, new_y, obstacle_1,
                            obstacle_2) and new_x != x_man:
            successors["Right"] = (new_x, new_y, obstacle_1, obstacle_2)
        # Left
        new_x = x_man - 1
        new_y = y_man
        obstacle_1 = self.move_obstacle(obstacle_1)
        obstacle_2 = self.move_obstacle(obstacle_2)
        if self.check_valid(new_x, new_y, obstacle_1,
                            obstacle_2) and new_x != x_man:
            successors["Left"] = (new_x, new_y, obstacle_1, obstacle_2)
        return successors

    @staticmethod
    def move_obstacle(obstacle):
        temp = list(obstacle)
        if temp[2] == 1:
            if temp[1] + 1 == 6:
                res = (temp[0], temp[1] - 1, -1)
                return res
            else:
                res = (temp[0], temp[1] + 1, 1)
                return res
        else:
            if temp[1] - 1 == -1:
                res = (temp[0], temp[1] + 1, 1)
                return res
            else:
                res = (temp[0], temp[1] - 1, -1)
                return res

    @staticmethod
    def check_valid(x_man, y_man, obstacle_1, obstacle_2):
        if (x_man, y_man) in obstacle_1 or (x_man, y_man) in obstacle_2:
            return False
        elif x_man < 0 or y_man < 0:
            return False
        elif x_man > 7 or y_man > 5:
            return False
        return True

    def actions(self, state):
        return self.successor(state).keys()

    def goal_test(self, state):
        return (state[0], state[1]) == self.goal

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        x_man = node.state[0]
        y_man = node.state[1]
        x_goal = self.goal[0]
        y_goal = self.goal[1]
        return abs(x_man - x_goal) + abs(y_man - y_goal)


if __name__ == '__main__':
    init = (0, 2)
    house = (7, 4)
    obstacle1 = (2, 5, -1)  # down
    obstacle2 = (5, 0, 1)  # up
    # (x,y,(o1x,o1y,o1d),(o2x,ob2y,o2d))
    explorer = Istrazuvac((init[0], init[1], obstacle1,
                           obstacle2), house)

    result = astar_search(explorer)
    print(result.solution())
