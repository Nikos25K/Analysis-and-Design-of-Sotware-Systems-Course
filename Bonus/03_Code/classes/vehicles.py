class Vehicle:
    def __init__(self, durability, capacity, movingSpeedFactor):
        self.durability = durability
        self.capacity = capacity
        self.carrying = 0
        self.movingSpeedFactor = movingSpeedFactor

    def getSpeedFactor(self):
        return self.movingSpeedFactor

    def get_durability(self):
        return self.durability

    def increase_durability(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            return

        if amount is None or amount <= 0:
            return

        self.durability += amount

    def decrease_durability(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            return

        if amount is None or amount <= 0:
            return

        self.durability -= amount
        if self.durability < 0:
            self.durability = 0

    def is_destroyed(self):
        return self.durability == 0


class LightVehicle(Vehicle):
    def __init__(self):
        super().__init__(durability=40, capacity=10, movingSpeedFactor=2)

class HeavyVehicle(Vehicle):
    def __init__(self):
        super().__init__(durability=100, capacity=20, movingSpeedFactor=1.4)

class ArmoredVehicle(Vehicle):
    def __init__(self):
        super().__init__(durability=150, capacity=15, movingSpeedFactor=1.2)