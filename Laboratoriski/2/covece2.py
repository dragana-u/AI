from searching_framework import Problem, astar_search


def move_right_2(covece_koord):
    res = (covece_koord[0] + 2, covece_koord[1])
    return res


def move_right_3(covece_koord):
    res = (covece_koord[0] + 3, covece_koord[1])
    return res


def move_up(covece_koord):
    res = (covece_koord[0], covece_koord[1] + 1)
    return res


def move_down(covece_koord):
    res = (covece_koord[0], covece_koord[1] - 1)
    return res


def move_left(covece_koord):
    res = (covece_koord[0] - 1, covece_koord[1])
    return res


class HomeGame(Problem):
    def __init__(self, initial, table_size, wall_positions, house):
        super().__init__(initial)
        self.table_size = table_size
        self.wall_positions = wall_positions
        self.house = house

    def check_valid(self, covece_koord):
        if covece_koord[0] < 0 or covece_koord[1] < 0:
            return False
        if covece_koord[0] > self.table_size - 1 or covece_koord[1] > self.table_size - 1:
            return False
        if covece_koord in self.wall_positions:
            return False
        return True

    def successor(self, state):
        successors = dict()
        covek = state

        # down
        new_state = move_down(covek)
        if self.check_valid(new_state):
            successors["Dolu"] = new_state

        # up
        new_state = move_up(covek)
        if self.check_valid(new_state):
            successors["Gore"] = new_state
        # left
        new_state = move_left(covek)
        if self.check_valid(new_state):
            successors["Levo"] = new_state
        # right 2
        new_state = move_right_2(covek)
        if self.check_valid(new_state) and (new_state[0] - 1, new_state[1]) not in self.wall_positions:
            successors["Desno 2"] = new_state
        # right 3
        new_state = move_right_3(covek)
        if (self.check_valid(new_state) and (new_state[0] - 1, new_state[1]) not in self.wall_positions and
                (new_state[0] - 2, new_state[1]) not in self.wall_positions and new_state[0] not in self.wall_positions):
            successors["Desno 3"] = new_state

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.house

    def h(self, node):
        x_covece = node.state[0]
        y_covece = node.state[1]
        x_house = self.house[0]
        y_house = self.house[1]

        return min(((abs(x_covece - x_house) + abs(y_covece - y_house)) / 3),
                   ((abs(x_covece - x_house) + abs(y_covece - y_house)) / 2))


if __name__ == '__main__':
    size_table = int(input())
    size_walls = int(input())
    walls = []
    for i in range(size_walls):
        x, y = map(int, input().split(","))
        walls.append((x, y))
    covece_x, covece_y = map(int, input().split(","))
    house_x, house_y = map(int, input().split(","))
    house_pos = (house_x, house_y)
    covece = (covece_x, covece_y)
    home_game = HomeGame(covece, size_table, tuple(walls), house_pos)
    result = astar_search(home_game)
    if result is not None:
        print(result.solution())
