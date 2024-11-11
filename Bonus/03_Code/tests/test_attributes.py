import pytest
import sys, os

# Add the directory containing the classes folder to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../classes')))

from animals import Deer, Wolf, Bear
from team import Team, Mechanic, Scout, Saboteur, Hunter
from vehicles import ArmoredVehicle, HeavyVehicle, LightVehicle
from world import Position, Plant, max_entity

# a parameterized test for the positions
@pytest.mark.parametrize("position, x, y", [
    (Position(12,13), 12, 13),
    (Position(0, 0), 0, 0),
    (Position(-5, 5), -5, 5)
])
def test_position(position, x, y):
    assert position.x == x
    assert position.y == y

# a parameterized test for the vehicles
@pytest.mark.parametrize("vehicle, durability, speed_factor", [
    (ArmoredVehicle(), 150, 1.2),
    (HeavyVehicle(), 100, 1.4),
    (LightVehicle(), 40, 2)
])
def test_vehicle(vehicle, durability, speed_factor):
    assert vehicle.get_durability() == durability
    assert vehicle.is_destroyed() == False
    assert vehicle.getSpeedFactor() == speed_factor

    vehicle.decrease_durability(150)
    assert vehicle.is_destroyed() == True


# a parameterized test for the plants
@pytest.mark.parametrize("plant, is_edible, position", [
    (Plant(Position(12,13), True), True, Position(12,13)),
    (Plant(Position(0, 0), False), False, Position(0, 0))
])
def test_plant(plant, is_edible, position):
    assert plant.is_edible() == is_edible
    assert plant.position == position

# some parameterized test for the teams
@pytest.mark.parametrize("member", [Scout(), Mechanic(), Saboteur(), Hunter()])
def test_add_and_remove_member(member):
    team = Team()
    team.add_member(member)
    assert member in team.members
    team.remove_member(member)
    assert member not in team.members

@pytest.mark.parametrize("vehicle", [LightVehicle(), HeavyVehicle(), ArmoredVehicle()])
def test_add_and_remove_vehicle(vehicle):
    team = Team()
    team.add_vehicle(vehicle)
    assert team.vehicle == vehicle
    team.remove_vehicle()
    assert team.vehicle is None

@pytest.mark.parametrize("new_position", [(10, 10), (0, 0), (-5, 5)])
def test_move(new_position):
    team = Team()
    team.move(new_position)
    assert team.get_position() == new_position

# parameterized test for the animals
@pytest.mark.parametrize("animal, attack_power, energy, position", [
    (Deer(Position(12,13)), 0, 0.5 * max_entity, Position(12,13)),
    (Wolf(Position(0, 0)), 1, 0.75 * max_entity, Position(0, 0)),
    (Bear(Position(-5, 5)), 3, max_entity, Position(-5, 5))
])
def test_animal(animal, attack_power, energy, position):
    assert animal.attack_power == attack_power
    assert animal.energy == energy
    assert animal.get_position() == position

    animal.move(Position(10, 10))
    assert animal.get_position() == Position(10, 10)

    animal.decrease_energy(1.1 * max_entity)
    assert animal.energy == 0
    assert animal.is_dead() == True

# tests for the decrease_energy function
@pytest.mark.parametrize("member", [Scout(), Mechanic(), Saboteur(), Hunter()])
def test_decrease_energy_member(member):
    team = Team()
    team.add_member(member)
    initial_energy = member.energy
    team.decrease_energy(1)
    assert member.energy == initial_energy - 1

# tests for the decrease_durability function
@pytest.mark.parametrize("vehicle", [LightVehicle(), HeavyVehicle(), ArmoredVehicle()])
def test_decrease_energy_vehicle(vehicle):
    initial_durability = vehicle.get_durability()
    vehicle.decrease_durability(1)
    assert vehicle.get_durability() == initial_durability - 1