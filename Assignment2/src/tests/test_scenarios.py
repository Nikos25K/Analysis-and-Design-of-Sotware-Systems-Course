import pytest

import sys, os

# Add the directory containing the classes folder to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../classes')))

from animals import Deer, Wolf, Bear
from team import Team, Trap, Mechanic, Scout, Hunter
from vehicles import ArmoredVehicle, LightVehicle, HeavyVehicle
from world import Position, Entropy, entropy

max_entity = 100

def test_Entropy():
    # simple creation
    ent = Entropy()
    assert ent.grade == 0

    # increase entropy
    ent.increaseEntropy(10)
    assert ent.grade == 10

    # decrease entropy
    ent.decrease()
    assert ent.grade == 9

    # increase entropy with negative value
    ent.increaseEntropy(-10)
    assert ent.grade == 9

    ent.increaseEntropy(100)
    assert ent.grade == 100

    # increase entropy while at max
    ent.increaseEntropy(1)
    assert ent.grade == 100

    # decrease entropy while at max
    ent.decrease()
    assert ent.grade == 100

def test_trap():
    # check if team not on trap then energy will not decrease
    team = Team()
    mechanic = Mechanic()
    assert mechanic.energy == max_entity
    team.add_member(mechanic)

    trap = Trap(Position(12,13), team)
    assert trap.position == Position(12,13)
    trap.isOnTrap(team)
    assert mechanic.energy == max_entity

    # move the team to the trap of the same team
    team.move(Position(12,13))
    trap.isOnTrap(team)
    assert mechanic.energy == max_entity
    team.move(Position(12,14))

    # create an enemy team and check if the trap will decrease energy of the member of the enemy team
    team2 = Team(Position(12,13))
    mechanic2 = Mechanic()
    assert mechanic2.energy == max_entity
    team2.add_member(mechanic2)

    trap.isOnTrap(team2)
    assert mechanic2.energy == max_entity - 5

    # now if the enemy team has a vehicle then the energy of the vehicle will not decrease
    vehicle = ArmoredVehicle()
    team2.add_vehicle(vehicle)
    trap.isOnTrap(team2)
    assert vehicle.get_durability() == 145
    assert mechanic2.energy == max_entity - 5

# tests for the repair_vehicle function
@pytest.mark.parametrize("member, vehicle", [
    (Mechanic(), LightVehicle()),
    (Mechanic(), HeavyVehicle()),
    (Mechanic(), ArmoredVehicle())
])
def test_repair_vehicle(member, vehicle):
    old_entropy = entropy.grade

    team = Team()
    team.add_member(member)
    team.add_vehicle(vehicle)
    vehicle.decrease_durability(10)
    initial_durability = vehicle.durability
    team.repair_vehicle()
    if isinstance(vehicle, LightVehicle):
        assert vehicle.durability == initial_durability + 20
    elif isinstance(vehicle, HeavyVehicle):
        assert vehicle.durability == initial_durability + 15
    else:
        assert vehicle.durability == initial_durability + 10

    # check if entropy is increased
    assert entropy.grade == old_entropy + 1

# test for activation of the hunter
def test_deadeye_shot():
    member = Hunter()
    team = Team()
    team.add_member(member)
    target = Bear()
    team.deadeye_shot(target)
    assert target.energy == 0.5 * max_entity

# test for activation of the scout
def test_invisible():
    member = Scout()
    team = Team()
    team.add_member(member)
    team.activate()
    assert team.timeInvisibleLeft == 60

# tests for the attack function of the animals
@pytest.mark.parametrize("animal", [Deer(), Wolf(), Bear()])
def test_attack_of_animal(animal):
    member = Hunter()
    team = Team()
    team.add_member(member)
    animal.attack(member)
    assert member.energy == max_entity - animal.attack_power