from world import max_entity, create_random_position, animals

class Animal:
    def __init__(self, position=None, attack_power=0, energy=max_entity):
        self.position = position if position is not None else create_random_position()
        self.attack_power = attack_power
        self.energy = energy
        animals.append(self)

    def move(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def get_energy(self):
        return self.energy

    def decrease_energy(self, amount=1):
        self.energy = self.energy - amount
        if self.energy < 0:
            self.energy = 0
            animals.remove(self)

    def is_dead(self):
        return self.energy == 0

    def attack(self, member):
        if member.is_dead() or self.is_dead() or self.attack_power == 0:
            return

        member.decrease_energy(self.attack_power)

# Two kinds of animals, one that does not attack and one that does attack members
class Deer(Animal):
    def __init__(self, position=None):
        super().__init__(position, 0, 0.5 * max_entity)

class Wolf(Animal):
    def __init__(self, position=None):
        super().__init__(position, 1, 0.75 * max_entity)

class Bear(Animal):
    def __init__(self, position=None):
        super().__init__(position, 3, max_entity)