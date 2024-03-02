class Agent:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Agent({self.x},{self.y})"

    def move(self):
        pass


class RightAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.x += 1


class LeftAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.x -= 1


class UpAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.y += 1


class DownAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.y -= 1


if __name__ == "__main__":
    leftAgent = LeftAgent(2, 3)
    rightAgent = RightAgent(4, 5)
    upAgent = UpAgent(-1, 0)
    downAgent = DownAgent(-5, -5)
    for i in range(5):
        leftAgent.move()
        print(f"Left  {leftAgent}")
        rightAgent.move()
        print(f"Right  {rightAgent}")
        upAgent.move()
        print(f"Up  {upAgent}")
        downAgent.move()
        print(f"Down  {downAgent}")

