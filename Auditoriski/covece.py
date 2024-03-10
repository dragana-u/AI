from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


class Istrazuvac(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.grid_size = [8, 6]

    def successor(self, state):
        successors = dict()
        covece_x = state[0]
        covece_y = state[1]

        obstacle1 = [state[2], state[3], state[4]]
        obstacle2 = [state[5], state[6], state[7]]

        self.dvizenje(obstacle1)
        self.dvizenje(obstacle2)

        obstacles = [(obstacle1[0], obstacle2[1]), (obstacle1[0]), (obstacle2[1])]
        # right
        if covece_x < self.grid_size[0] - 1 and [covece_x + 1, covece_y] not in obstacles:  # right
            successors['Right'] = (covece_x + 1, covece_y,
                                   obstacle1[0], obstacle1[1], obstacle1[2],
                                   obstacle2[0], obstacle2[1], obstacle2[2])

        if covece_x > 0 and [covece_x - 1, covece_y] not in obstacles:  # left
            successors['Left'] = (covece_x - 1, covece_y,
                                  obstacle1[0], obstacle1[1], obstacle1[2],
                                  obstacle2[0], obstacle2[1], obstacle2[2])

        if covece_y < self.grid_size[1] - 1 and [covece_x, covece_y + 1] not in obstacles:  # up
            successors['Up'] = (covece_x, covece_y + 1,
                                obstacle1[0], obstacle1[1], obstacle1[2],
                                obstacle2[0], obstacle2[1], obstacle2[2])

        if covece_y > 0 and [covece_x, covece_y - 1] not in obstacles:  # down
            successors['Down'] = (covece_x, covece_y - 1,
                                  obstacle1[0], obstacle1[1], obstacle1[2],
                                  obstacle2[0], obstacle2[1], obstacle2[2])

        return successors

    def dvizenje(self, obstacle):
        obstacle = list(obstacle)
        if obstacle[2] == 1:  # up
            if obstacle[1] == self.grid_size[1] - 1:
                obstacle[2] = -1
                obstacle[1] -= 1
            else:
                obstacle[1] += 1
        else:  # down
            if obstacle[1] == 0:
                obstacle[2] = 1
                obstacle[1] += 1
            else:
                obstacle[1] -= 1

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        position = (state[0], state[1])
        return position == self.goal


if __name__ == '__main__':
    goal_state = (7, 4)
    initial_state = (0, 2)
    obstacle_1 = (2, 5, 1)  # down
    obstacle_2 = (5, 0, 0)  # up

    explorer = Istrazuvac((initial_state[0], initial_state[1],
                           obstacle_1[0], obstacle_1[1], obstacle_1[2],
                           obstacle_2[0], obstacle_2[1], obstacle_2[2]), goal_state)

    print(breadth_first_graph_search(explorer).solution())
    print(breadth_first_graph_search(explorer).solve())
