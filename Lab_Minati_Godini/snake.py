from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

class Snake(Problem):

    def __init__(self, initial, red_apples, goal=None):
        super().__init__(initial, goal)
        self.red_apples = red

    def successor(self, state):
        successors = dict()

        snake = state[0]
        green_apples = state[1]
        orientation = state[2]

        new_snake, new_apples, new_orientation = ProdolzhiPravo(snake, green_apples, self.red_apples, orientation)
        if new_snake != snake:
            successors['ProdolzhiPravo'] = (new_snake, new_apples, new_orientation)

        new_snake, new_apples, new_orientation = SvrtiDesno(snake, green_apples, self.red_apples, orientation)
        if new_snake != snake:
            successors['SvrtiDesno'] = (new_snake, new_apples, new_orientation)

        new_snake, new_apples, new_orientation = SvrtiLevo(snake, green_apples, self.red_apples, orientation)
        if new_snake != snake:
            successors['SvrtiLevo'] = (new_snake, new_apples, new_orientation)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[1]) == 0


def ProdolzhiPravo(snake, green_apples, red_apples, orientation):
    head = snake[-1]
    if orientation == 'dolu':
        if head[1] - 1 >= 0 and (head[0], head[1] - 1) not in red_apples and (head[0], head[1] - 1) not in snake:
            snake = list(snake)
            snake.append((head[0], head[1] - 1))

            if (head[0], head[1] - 1) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake]
                green_apples = tuple(green_apples)
            else:
                snake = snake[1:]
            snake = tuple(snake)
    elif orientation == 'gore':
        if head[1] + 1 < 10 and (head[0], head[1] + 1) not in red_apples and (head[0], head[1] + 1) not in snake:
            snake = list(snake)
            snake.append((head[0], head[1] + 1))

            if (head[0], head[1] + 1) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake]
                green_apples = tuple(green_apples)
            else:
                snake = snake[1:]
            snake = tuple(snake)
    elif orientation == 'desno':
        if head[0] + 1 < 10 and (head[0] + 1, head[1]) not in red_apples and (head[0] + 1, head[1]) not in snake:
            snake = list(snake)
            snake.append((head[0] + 1, head[1]))

            if (head[0] + 1, head[1]) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake]
                green_apples = tuple(green_apples)
            else:
                snake = snake[1:]
            snake = tuple(snake)
    elif orientation == 'levo':
        if head[0] - 1 >= 0 and (head[0] - 1, head[1]) not in red_apples and (head[0] - 1, head[1]) not in snake:
            snake = list(snake)
            snake.append((head[0] - 1, head[1]))

            if (head[0] - 1, head[1]) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake]
                green_apples = tuple(green_apples)
            else:
                snake = snake[1:]
            snake = tuple(snake)

    return snake, green_apples, orientation


def SvrtiDesno(snake, green_apples, red_apples, orientation):
    head = snake[-1]
    if orientation == 'desno':
        if head[1] - 1 >= 0 and (head[0], head[1] - 1) not in red_apples and (head[0], head[1] - 1) not in snake:
            snake = list(snake)
            snake.append((head[0], head[1] - 1))

            if (head[0], head[1] - 1) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake]
                green_apples = tuple(green_apples)
            else:
                snake = snake[1:]
            snake = tuple(snake)
            orientation = 'dolu'
    elif orientation == 'levo':
        if head[1] + 1 < 10 and (head[0], head[1] + 1) not in red_apples and (head[0], head[1] + 1) not in snake:
            snake = list(snake)
            snake.append((head[0], head[1] + 1))

            if (head[0], head[1] + 1) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake]
                green_apples = tuple(green_apples)
            else:
                snake = snake[1:]
            snake = tuple(snake)
            orientation = 'gore'
    elif orientation == 'gore':
        if head[0] + 1 < 10 and (head[0] + 1, head[1]) not in red_apples and (head[0] + 1, head[1]) not in snake:
            snake = list(snake)
            snake.append((head[0] + 1, head[1]))

            if (head[0] + 1, head[1]) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake]
                green_apples = tuple(green_apples)
            else:
                snake = snake[1:]
            snake = tuple(snake)
            orientation = 'desno'
    elif orientation == 'dolu':
        if head[0] - 1 >= 0 and (head[0] - 1, head[1]) not in red_apples and (head[0] - 1, head[1]) not in snake:
            snake = list(snake)
            snake.append((head[0] - 1, head[1]))

            if (head[0] - 1, head[1]) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake]
                green_apples = tuple(green_apples)
            else:
                snake = snake[1:]
            snake = tuple(snake)
            orientation = 'levo'

    return snake, green_apples, orientation


def SvrtiLevo(snake, green_apples, red_apples, orientation):
    head = snake[-1]
    if orientation == 'levo':
        if head[1] - 1 >= 0 and (head[0], head[1] - 1) not in red_apples and (head[0], head[1] - 1) not in snake:
            snake = list(snake)
            snake.append((head[0], head[1] - 1))

            if (head[0], head[1] - 1) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake]
                green_apples = tuple(green_apples)
            else:
                snake = snake[1:]
            snake = tuple(snake)
            orientation = 'dolu'
    elif orientation == 'desno':
        if head[1] + 1 < 10 and (head[0], head[1] + 1) not in red_apples and (head[0], head[1] + 1) not in snake:
            snake = list(snake)
            snake.append((head[0], head[1] + 1))

            if (head[0], head[1] + 1) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake]
                green_apples = tuple(green_apples)
            else:
                snake = snake[1:]
            snake = tuple(snake)
            orientation = 'gore'
    elif orientation == 'dolu':
        if head[0] + 1 < 10 and (head[0] + 1, head[1]) not in red_apples and (head[0] + 1, head[1]) not in snake:
            snake = list(snake)
            snake.append((head[0] + 1, head[1]))

            if (head[0] + 1, head[1]) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake]
                green_apples = tuple(green_apples)
            else:
                snake = snake[1:]
            snake = tuple(snake)
            orientation = 'desno'
    elif orientation == 'gore':
        if head[0] - 1 >= 0 and (head[0] - 1, head[1]) not in red_apples and (head[0] - 1, head[1]) not in snake:
            snake = list(snake)
            snake.append((head[0] - 1, head[1]))

            if (head[0] - 1, head[1]) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake]
                green_apples = tuple(green_apples)
            else:
                snake = snake[1:]
            snake = tuple(snake)
            orientation = 'levo'

    return snake, green_apples, orientation

if __name__ == '__main__':
    n = int(input())
    green = []

    for i in range(0, n):
        apple = input().split(',')
        apple = [int(apple[0]), int(apple[1])]
        green.append(tuple(apple))

    m = int(input())
    red = []

    for i in range(0, m):
        apple = input().split(',')
        apple = [int(apple[0]), int(apple[1])]
        red.append(tuple(apple))

    s = ((0, 9), (0, 8), (0, 7))
    orien = 'dolu'

    snake_problem = Snake((s, tuple(green), orien), tuple(red))
    print(breadth_first_graph_search(snake_problem).solution())