from Figure import Figure
from Direction import Direction
from Map import Map

class MovableFigure(Figure):
    def __init__(self, coordinates, width, height, speed, weight = 0):
        super().__init__(coordinates, width, height)
        self.speed = speed
        self.weight = weight

    def move(self, direction, map):
        if(self.weight > 0):
            self.coordinates.y = self.coordinates.y + self.weight
        self.moveOnDirection(direction)
        self.correctCoordinates(map)

    def correctCoordinates(self, map):
        self.coordinates.y = max(0, self.coordinates.y)
        self.coordinates.y = min(map.height - self.height, self.coordinates.y)

        self.coordinates.x = max(0, self.coordinates.x)
        self.coordinates.x = min(map.width - self.width, self.coordinates.x)

    def moveOnDirection(self, direction):
        if direction == Direction.UP:
            self.coordinates.y -= self.speed
        if direction == Direction.DOWN:
            self.coordinates.y += self.speed
        if direction == Direction.LEFT:
            self.coordinates.x -= self.speed
        if direction == Direction.RIGHT:
            self.coordinates.x += self.speed
