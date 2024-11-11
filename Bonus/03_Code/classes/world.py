import random

def create_random_position():
    from world import Position
    return Position(random.randint(0, 100), random.randint(0, 100))

max_entity = 100
max_entropy = 100

class Entropy:
    def __init__(self):
        self.grade = 0

    def increaseEntropy(self, amount=None):
        if amount is None:
            return

        try:
            amount = int(amount)
        except ValueError:
            return

        if amount <= 0:
            return

        if self.grade + amount > max_entropy:
            self.grade = max_entropy
            # print("Entropy is at maximum level")
        else:
            self.grade += amount

    def decrease(self):
        if self.grade == max_entropy:
            return

        if self.grade - 1 < 0:
            self.grade = 0
        else:
            self.grade -= 1

class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Position):
            return False
        return self.x == other.x and self.y == other.y

class Plant:
    def __init__(self, position=None, isEdible=False):
        self.position = position if position is not None else create_random_position()
        self.isEdible = isEdible

    def is_edible(self):
        return self.isEdible

class Key:
    def __init__(self, position=None):
        if position is None:
            position = Position()
        self.position = position if position is not None else create_random_position()

    def get_distance_from_key(self, position):
        return abs(self.position.x - position.x) + abs(self.position.y - position.y)

animals = []
teams = []
plants = []

entropy = Entropy()
key = Key()