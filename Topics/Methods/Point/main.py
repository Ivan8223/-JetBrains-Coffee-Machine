class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, another_point):
        return (
            (self.x - another_point.x) ** 2
            + (self.y - another_point.y) ** 2
        ) ** 0.5
