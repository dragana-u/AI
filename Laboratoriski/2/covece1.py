from searching_framework import Problem, astar_search


def pridvizi_kukja(kukja_pos):
    kukja_pos = list(kukja_pos)
    if kukja_pos[2] == "desno":
        if kukja_pos[0] + 1 == 5:
            kukja_pos[2] = "levo"
            res = (kukja_pos[0] - 1, kukja_pos[1], kukja_pos[2])
            return res
        else:
            res = (kukja_pos[0] + 1, kukja_pos[1], kukja_pos[2])
            return res
    else:  # levo
        if kukja_pos[0] - 1 == -1:
            kukja_pos[2] = "desno"
            res = (kukja_pos[0] + 1, kukja_pos[1], kukja_pos[2])
            return res
        else:
            res = (kukja_pos[0] - 1, kukja_pos[1], kukja_pos[2])
            return res


def covece_gore_1(covece_x, covece_y):
    res = (covece_x, covece_y + 1)
    return res


def covece_gore_2(covece_x, covece_y):
    res = (covece_x, covece_y + 2)
    return res


def covece_gore_desno_1(covece_x, covece_y):
    res = (covece_x + 1, covece_y + 1)
    return res


def covece_gore_desno_2(covece_x, covece_y):
    res = (covece_x + 2, covece_y + 2)
    return res


def covece_gore_levo_1(covece_x, covece_y):
    res = (covece_x - 1, covece_y + 1)
    return res


def covece_gore_levo_2(covece_x, covece_y):
    res = (covece_x - 2, covece_y + 2)
    return res


class HouseGame(Problem):
    def __init__(self, initial, allowed_pos):
        super().__init__(initial)
        self.allowed_pos = allowed_pos
        self.width = 5
        self.height = 9

    def check_valid(self, covece_x, covece_y, kukja_pos):
        allowed_kukja = list(self.allowed_pos)
        allowed_kukja.append((kukja_pos[0], kukja_pos[1]))
        allowed_kukja = tuple(allowed_kukja)
        if covece_x < 0 or covece_x > self.width:
            return False
        if covece_y < 0 or covece_y > self.height:
            return False
        if (covece_x, covece_y) not in allowed_kukja:
            return False
        return True

    def successor(self, state):
        successors = dict()

        covece_x, covece_y = state[0][0], state[0][1]
        kukja_x, kukja_y = state[1][0], state[1][1]
        kukja_orient = state[1][2]

        # Stoj
        kukja_pos = pridvizi_kukja((kukja_x, kukja_y, kukja_orient))
        successors["Stoj"] = ((covece_x, covece_y), kukja_pos)

        # Gore 1
        kukja_pos = pridvizi_kukja((kukja_x, kukja_y, kukja_orient))
        new_state = (covece_gore_1(covece_x, covece_y), kukja_pos)
        if self.check_valid(new_state[0][0], new_state[0][1], kukja_pos):
            successors["Gore 1"] = new_state

        # Gore 2
        kukja_pos = pridvizi_kukja((kukja_x, kukja_y, kukja_orient))
        new_state = (covece_gore_2(covece_x, covece_y), kukja_pos)
        if self.check_valid(new_state[0][0], new_state[0][1], kukja_pos):
            successors["Gore 2"] = new_state

        # Gore-desno 1
        kukja_pos = pridvizi_kukja((kukja_x, kukja_y, kukja_orient))
        new_state = (covece_gore_desno_1(covece_x, covece_y), kukja_pos)
        if self.check_valid(new_state[0][0], new_state[0][1], kukja_pos):
            successors["Gore-desno 1"] = new_state

        # Gore-desno 2
        kukja_pos = pridvizi_kukja((kukja_x, kukja_y, kukja_orient))
        new_state = (covece_gore_desno_2(covece_x, covece_y), kukja_pos)
        if self.check_valid(new_state[0][0], new_state[0][1], kukja_pos):
            successors["Gore-desno 2"] = new_state

        # Gore-levo 1
        kukja_pos = pridvizi_kukja((kukja_x, kukja_y, kukja_orient))
        new_state = (covece_gore_levo_1(covece_x, covece_y), kukja_pos)
        if self.check_valid(new_state[0][0], new_state[0][1], kukja_pos):
            successors["Gore-levo 1"] = new_state

        # Gore-levo 2
        kukja_pos = pridvizi_kukja((kukja_x, kukja_y, kukja_orient))
        new_state = (covece_gore_levo_2(covece_x, covece_y), kukja_pos)
        if self.check_valid(new_state[0][0], new_state[0][1], kukja_pos):
            successors["Gore-levo 2"] = new_state
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0][0] == state[1][0] and state[0][1] == state[1][1]

    def h(self, node):
        value = 0
        covece_x, covece_y = node.state[0][0], node.state[0][1]
        for a in allowed:
            if a[0] > covece_x and a[1] == covece_y:
                value += 1
        return value


if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]
    covece = input().split(",")
    covece = [int(c) for c in covece]
    covece = tuple(covece)
    kukja = input().split(",")
    kukja = [int(k) for k in kukja]
    kukja.append(input())
    kukja = tuple(kukja)
    house_game = HouseGame((covece, kukja), tuple(allowed))
    result = astar_search(house_game)
    if result is not None:
        print(result.solution())
