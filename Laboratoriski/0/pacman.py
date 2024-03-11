import random
import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"
random.seed(0)


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, position):
        self.x = position[0]
        self.y = position[1]
        print(f"[{self.x}, {self.y}]")


class Game:
    def __init__(self, width, height, matrix):
        self.width = width
        self.height = height
        self.matrix = matrix


class Pacman:
    def __init__(self, width, height, matrix):
        self.player = Player(0, 0)
        self.game = Game(width, height, matrix)
        self.desired = self.desired_positions()

    def play_game(self):
        if len(self.desired) == 0:
            print("Nothing to do here")
            return
        while len(self.desired) != 0:
            x_coord = self.player.x
            y_coord = self.player.y
            if (x_coord, y_coord) in self.desired:
                self.desired.remove((x_coord, y_coord))

            elif (x_coord+1, y_coord) in self.desired:
                self.desired.remove((x_coord+1, y_coord))
                self.player.move((x_coord+1, y_coord))

            elif (x_coord-1, y_coord) in self.desired:
                self.desired.remove((x_coord-1, y_coord))
                self.player.move((x_coord-1, y_coord))

            elif (x_coord, y_coord+1) in self.desired:
                self.desired.remove((x_coord, y_coord+1))
                self.player.move((x_coord, y_coord+1))

            elif (x_coord, y_coord-1) in self.desired:
                self.desired.remove((x_coord, y_coord-1))
                self.player.move((x_coord, y_coord-1))

            else:
                if x_coord > 0:
                    self.player.move((x_coord - 1, y_coord))
                elif x_coord < self.game.width - 1:
                    self.player.move((x_coord + 1, y_coord))
                elif y_coord > 0:
                    self.player.move((x_coord, y_coord - 1))
                elif y_coord < self.game.height - 1:
                    self.player.move((x_coord, y_coord + 1))

    def desired_positions(self):
        pos = []
        for i in range(self.game.width):
            for j in range(self.game.height):
                if self.game.matrix[i][j] == '.':
                    pos.append((i, j))
        return pos


if __name__ == "__main__":
    w = int(input())
    h = int(input())
    mat = []
    for _ in range(h):
        mat.append(list(input().strip()))
    pacman = Pacman(w, h, mat)
    pacman.play_game()
