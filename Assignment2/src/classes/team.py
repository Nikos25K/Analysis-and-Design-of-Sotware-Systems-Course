import random

from world import max_entity, create_random_position, entropy
from animals import Animal
from vehicles import LightVehicle, HeavyVehicle

class Team:
    def __init__(self, position=None):
        self.members = []
        self.position = position if position is not None \
            else create_random_position()
        self.vehicle = None
        self.timeInvisibleLeft = 0
        self.movingSpeed = 1

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        self.members.remove(member)

    def add_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.movingSpeed = self.movingSpeed * self.vehicle.getSpeedFactor()

    def remove_vehicle(self):
        self.vehicle = None

    def get_position(self):
        return self.position

    def move(self, position):
        self.position = position

    #choose a random member and decrease its energy
    def decrease_energy(self, amount=1):
        if len(self.members) == 0:
            return

        if self.vehicle is not None:
            self.vehicle.decrease_durability(amount)
            if self.vehicle.get_durability() == 0:
                self.vehicle = None
                self.movingSpeed = 1
                self.timeInvisibleLeft = 0
            return

        member = random.choice(self.members)
        member.decrease_energy(amount)

    def check_valid_member(self, member):
        for m in self.members:
            if isinstance(m, member) and not m.is_dead() and m.can_be_activated():
                return m
        return None

    def set_trap(self):
        m = self.check_valid_member(Saboteur)
        if m is not None:
            m.set_trap(self.position)

    def repair_vehicle(self):
        m = self.check_valid_member(Mechanic)
        if m is not None:
            m.repair_vehicle(self.vehicle)

    def deadeye_shot(self, target):
        m = self.check_valid_member(Hunter)
        if m is not None:
            m.deadeye_shot(target)

    def activate(self):
        m = self.check_valid_member(Scout)
        if m is not None:
            m.activate()
            self.timeInvisibleLeft = 60

class Member:
    def __init__(self):
        self.energy = max_entity
        self.timeToActivate = 0

    def is_dead(self):
        return self.energy == 0

    def decrease_energy(self, amount=1):
        self.energy = self.energy - amount
        if self.energy < 0:
            self.energy = 0

    def can_be_activated(self):
        return self.timeToActivate == 0

class Scout(Member):
    def __init__(self):
        super().__init__()

    def activate(self):
        self.timeToActivate = 60
        entropy.increaseEntropy(1)

class Mechanic(Member):
    def __init__(self):
        super().__init__()

    def repair_vehicle(self, vehicle):
        if vehicle is None:
            return

        if isinstance(vehicle, LightVehicle):
            new_durability = 20
        elif isinstance(vehicle, HeavyVehicle):
            new_durability = 15
        else:
            new_durability = 10

        vehicle.increase_durability(new_durability)
        self.timeToActivate = 60
        entropy.increaseEntropy(1)

class Saboteur(Member):
    def __init__(self):
        super().__init__()

    def set_trap(self, position):
        new_trap = Trap(position)
        self.timeToActivate = 60
        entropy.increaseEntropy(1)

class Hunter(Member):
    def __init__(self):
        super().__init__()

    def deadeye_shot(self, target):
        if target.is_dead():
            return 0

        # check class type of target
        if isinstance(target, Animal):
            target.decrease_energy(0.5 * max_entity)
        else:
            target.decrease_energy(5)

        entropy.increaseEntropy(1)
        self.timeToActivate = 60
        return 0

class Trap:
    def __init__(self, position=None, Team=None):
        self.team = Team if Team is not None else None
        self.position = position if position is not None else create_random_position()

    def isOnTrap(self, target):
        if target is None:
            return

        if isinstance(target, Team) and target != self.team:
            if target.get_position() == self.position:
                target.decrease_energy(5)